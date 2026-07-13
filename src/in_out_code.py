"""Compatibility import for the bundled incidence-direction algorithm."""

from get_in_out_code.src.get_in_out_code import get_in_out_code


def in_out_code(pd_code: list[list[int]]) -> list[list[str]]:
    """Return the incidence directions of a canonical knot PD code."""

    return get_in_out_code(pd_code)
