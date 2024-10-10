#!/usr/bin/env python3
'''type-annotated function sum_mixed_list'''
from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    '''function sum_mixed_list'''
    return float(sum(mxd_lst))
