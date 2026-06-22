# Copyright (c) 2026 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

from launch import Action
from launch.actions import SetLaunchConfiguration
from launch.launch_context import LaunchContext
from launch.logging import get_logger
from rcl_interfaces.msg import Parameter, ParameterValue
import rcl_interfaces.srv
import rclpy
from rclpy.parameter import ParameterType


class GetParametersFromBlackboard(Action):
    """
    Fetch parameters from a running node.

    Store each fetched parameter as a new LaunchConfiguration.
    """

    def __init__(
        self,
        blackboard_node_name: str,
        parameter_names: list[str],
        default_values: dict = None,
        **kwargs
    ):
        """
        Construct the action.

        :param blackboard_node_name: The name of the node to get the parameter from.
        :param parameter_names: A list of parameter names to fetch.
        :param default_values: A dictionary mapping parameter names to default values
                               to use if a parameter cannot be fetched.
        """
        super().__init__(**kwargs)
        self._blackboard_node_name = blackboard_node_name
        self._parameter_names = parameter_names
        self._default_values = default_values if default_values is not None else {}
        self._logger = get_logger('GetParametersFromBlackboard')

    def _get_value_as_string(self, param_value) -> str:
        """Convert a parameter value to a string."""
        if param_value.type == ParameterType.PARAMETER_STRING:
            return param_value.string_value
        elif param_value.type == ParameterType.PARAMETER_BOOL:
            return str(param_value.bool_value)
        elif param_value.type == ParameterType.PARAMETER_INTEGER:
            return str(param_value.integer_value)
        elif param_value.type == ParameterType.PARAMETER_DOUBLE:
            return str(param_value.double_value)
        # Add other types like arrays if needed
        return ''

    def execute(self, context: LaunchContext):
        """Execute this action in the launch system."""
        actions_to_return = []

        # Only initialise rclpy if it is not already running (e.g. when invoked from
        # launch_testing, which initialises rclpy before the test suite runs).
        rclpy_initialized_here = not rclpy.ok()
        if rclpy_initialized_here:
            rclpy.init()
        try:
            temp_node = rclpy.create_node('temporary_param_fetcher')
            client = temp_node.create_client(
                rcl_interfaces.srv.GetParameters, f'/{self._blackboard_node_name}/get_parameters')

            if not client.wait_for_service(timeout_sec=3.0):
                self._logger.error(
                    f"Parameter blackboard '{self._blackboard_node_name}' not available. "
                    'Using default values for all requested parameters.')
                # If blackboard is down, set all params to their defaults
                for param_name in self._parameter_names:
                    default = self._default_values.get(param_name, '')
                    actions_to_return.append(SetLaunchConfiguration(name=param_name,
                                                                    value=default))
                return actions_to_return

            # If blackboard is up, make a single request for all parameters
            request = rcl_interfaces.srv.GetParameters.Request()
            request.names = self._parameter_names

            future = client.call_async(request)
            rclpy.spin_until_future_complete(temp_node, future, timeout_sec=3.0)

            if future.result():
                # The response is a list of values in the same order as the request
                for i, param_name in enumerate(self._parameter_names):
                    param_value = future.result().values[i]

                    if param_value.type != ParameterType.PARAMETER_NOT_SET:
                        fetched_value = self._get_value_as_string(param_value)
                        self._logger.info(
                            f"Fetched '{param_name}' = '{fetched_value}'. "
                            'Setting LaunchConfiguration.')
                        actions_to_return.append(SetLaunchConfiguration(name=param_name,
                                                                        value=fetched_value))
                    else:
                        default = self._default_values.get(param_name, '')
                        self._logger.warn(
                            f"Could not fetch '{param_name}'. Using default value '{default}'.")
                        actions_to_return.append(SetLaunchConfiguration(name=param_name,
                                                                        value=default))
            else:
                self._logger.error('Service call to get parameters failed.')
                # Fallback to defaults if the call itself fails
                for param_name in self._parameter_names:
                    default = self._default_values.get(param_name, '')
                    actions_to_return.append(SetLaunchConfiguration(name=param_name,
                                                                    value=default))

        finally:
            temp_node.destroy_node()
            if rclpy_initialized_here:
                rclpy.shutdown()

        return actions_to_return


class SetParametersToBlackboard(Action):
    """
    Set parameters on a running node.

    Resolve LaunchConfigurations before sending parameter values.
    """

    def __init__(
        self,
        blackboard_node_name: str,
        parameters: dict[str, Any],
        **kwargs
    ):
        """
        Construct the action.

        :param blackboard_node_name: The name of the node to set parameters on.
        :param parameters: A dictionary mapping the desired parameter name (str)
                           to a Substitution (e.g., LaunchConfiguration) that
                           will provide the value.
        """
        super().__init__(**kwargs)
        self._blackboard_node_name = blackboard_node_name
        self._parameters = parameters
        self._logger = get_logger('SetParametersToBlackboard')

    def _string_to_parameter_value(self, value: str) -> ParameterValue:
        """
        Convert a string to the most appropriate ParameterValue type.

        Infer bool, int, double, or string values.
        """
        if value.lower() == 'true':
            return ParameterValue(type=ParameterType.PARAMETER_BOOL, bool_value=True)
        if value.lower() == 'false':
            return ParameterValue(type=ParameterType.PARAMETER_BOOL, bool_value=False)
        try:
            return ParameterValue(type=ParameterType.PARAMETER_INTEGER, integer_value=int(value))
        except ValueError:
            pass
        try:
            return ParameterValue(type=ParameterType.PARAMETER_DOUBLE, double_value=float(value))
        except ValueError:
            pass
        return ParameterValue(type=ParameterType.PARAMETER_STRING, string_value=value)

    def execute(self, context: LaunchContext):
        """Execute this action in the launch system."""
        # Only initialise rclpy if it is not already running (e.g. when invoked from
        # launch_testing, which initialises rclpy before the test suite runs).
        rclpy_initialized_here = not rclpy.ok()
        if rclpy_initialized_here:
            rclpy.init()
        try:
            temp_node = rclpy.create_node('temporary_param_setter')
            client = temp_node.create_client(
                rcl_interfaces.srv.SetParameters, f'/{self._blackboard_node_name}/set_parameters')

            if not client.wait_for_service(timeout_sec=5.0):
                self._logger.error(
                    f"Parameter blackboard '{self._blackboard_node_name}' not available. "
                    'Cannot set parameters.')
                return

            request = rcl_interfaces.srv.SetParameters.Request()

            # Resolve substitutions and build the list of parameters
            for name, value_substitution in self._parameters.items():
                resolved_value = value_substitution.perform(context)
                self._logger.info(f"Preparing to set parameter '{name}' to '{resolved_value}'")
                param_msg = Parameter(
                    name=name,
                    value=self._string_to_parameter_value(resolved_value)
                )
                request.parameters.append(param_msg)

            if not request.parameters:
                self._logger.warn('No parameters provided to set.')
                return

            future = client.call_async(request)
            rclpy.spin_until_future_complete(temp_node, future, timeout_sec=5.0)

            if future.result():
                for i, result in enumerate(future.result().results):
                    param_name = request.parameters[i].name
                    if result.successful:
                        self._logger.info(f"Successfully set parameter '{param_name}'.")
                    else:
                        self._logger.error(
                            f"Failed to set parameter '{param_name}': {result.reason}")
            else:
                self._logger.error(f'Service call to set parameters failed: {future.exception()}')

        finally:
            temp_node.destroy_node()
            if rclpy_initialized_here:
                rclpy.shutdown()

        # This action has a side effect and doesn't add other actions to the launch
        return None
