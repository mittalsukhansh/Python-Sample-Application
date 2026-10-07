"""
Dummy features module for git branch/merge practice.

This file contains simple, independent functions that different branches
can modify to create harmless merge scenarios for practice.

Usage:
	python features.py [feature_a|feature_b|feature_c]
"""

import sys


def feature_a(x: int) -> int:
	"""Simple feature A: multiply by 2."""
	return x * 2


def feature_b(x: int) -> int:
	"""Simple feature B: add 10."""
	return x + 10


def feature_c(x: int) -> str:
	"""Simple feature C: return a formatted string."""
	return f"Value is: {x}"


def main(argv=None):
	argv = argv or sys.argv[1:]
	if not argv:
		print("Specify a feature: feature_a, feature_b, or feature_c")
		return

	name = argv[0]
	try:
		value = int(argv[1]) if len(argv) > 1 else 5
	except ValueError:
		print("Second argument must be an integer")
		return

	if name == "feature_a":
		print(feature_a(value))
	elif name == "feature_b":
		print(feature_b(value))
	elif name == "feature_c":
		print(feature_c(value))
	else:
		print("Unknown feature")


if __name__ == "__main__":
	main()
