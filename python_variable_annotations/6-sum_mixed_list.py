#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Args:
        mxd_lst (List[Union[int, float]]): _description_

    Returns:
        float: sum as a float
    """
    return sum(mxd_lst)
