#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


class YamlIO:
    """Load and dump YAML files with basic safety.

    Methods:
        load(path): Load a YAML file into a Python dictionary.
        dump(data, path): Dump a Python dictionary to a YAML file.
    """

    @staticmethod
    def load(path: Path) -> dict[str, Any]:
        """Load a YAML file into a Python dictionary.

        Args:
            path: Path to the YAML file.

        Returns:
            A dictionary representing the YAML content.

        Raises:
            FileNotFoundError: If the file does not exist.
            yaml.YAMLError: If the YAML content is invalid.
        """
        if not path.is_file():
            raise FileNotFoundError(f"Input file not found: {path}")
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            raise yaml.YAMLError("Top-level YAML content must be a mapping.")
        return data

    @staticmethod
    def dump(data: dict[str, Any], path: Path) -> None:
        """Dump a Python dictionary to a YAML file.

        Args:
            data: The data to serialize.
            path: Output path for the YAML file.

        Returns:
            None

        Raises:
            OSError: If the file cannot be written.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
        return None


class MotionFormatTransformer:
    """Transform motion entries by flattening points into times and positions.

    Methods:
        transform(data): Transform the entire YAML payload.
    """

    def transform(self, data: dict[str, Any]) -> dict[str, Any]:
        """Transform the entire YAML payload.

        Args:
            data: The original YAML mapping keyed by motion names.

        Returns:
            A new mapping with flattened time and position sequences.

        Raises:
            ValueError: If required fields are missing or invalid.
        """
        result: dict[str, Any] = {}
        for motion_name, motion in data.items():
            if not isinstance(motion, dict):
                raise ValueError(f"Motion '{motion_name}' must be a mapping.")
            joints = motion.get("joints")
            points = motion.get("points")
            meta = motion.get("meta", {})
            if not isinstance(joints, list):
                raise ValueError(f"Motion '{motion_name}' must contain a 'joints' list.")
            if not isinstance(points, list) or len(points) == 0:
                raise ValueError(f"Motion '{motion_name}' must contain a non-empty 'points' list.")
            times_from_start: list[float | int] = []
            positions: list[float] = []
            for idx, point in enumerate(points):
                if not isinstance(point, dict):
                    raise ValueError(f"Point {idx} in '{motion_name}' must be a mapping.")
                t = point.get("time_from_start")
                pos = point.get("positions")
                if t is None:
                    raise ValueError(f"Point {idx} in '{motion_name}' lacks 'time_from_start'.")
                if not isinstance(pos, list) or not all(isinstance(x, (int, float)) for x in pos):
                    raise ValueError(f"Point {idx} in '{motion_name}' has invalid 'positions'.")
                times_from_start.append(t)
                positions.extend(float(x) for x in pos)
            result[motion_name] = {
                "joints": joints,
                "times_from_start": times_from_start,
                "positions": positions,
                "meta": meta,
            }
        return result


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser.

    Returns:
        An argparse.ArgumentParser configured for this application.
    """
    parser = argparse.ArgumentParser(
        description="Flatten 'points' into 'times_from_start' and concatenated 'positions' in a motion YAML."
    )
    parser.add_argument("input", type=Path, help="Path to the input YAML file.")
    parser.add_argument("output", type=Path, help="Path to the output YAML file.")
    return parser


def main() -> None:
    """Entry point for the motion YAML transformer.

    Reads the input YAML, applies the transformation, and writes the output YAML.
    """
    args = build_parser().parse_args()
    original = YamlIO.load(args.input)
    transformed = MotionFormatTransformer().transform(original)
    YamlIO.dump(transformed, args.output)


if __name__ == "__main__":
    main()
