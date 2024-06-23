import sys
import numpy as np


"""
    This function does not slice the 2d array , it actually only
    selects particular row and colums xd
"""

def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert isinstance(start, int) , "Start is not an int"
        assert isinstance(end, int) , "End is not an int"
        assert isinstance(family, list) , "Family is not a list"
        np_family = np.array(family)
        assert np.array(family).ndim == 2 , "The family is not 2D array"
        shape = np_family.shape
        print(f"My shape is : {shape}")
        new_family = np_family[start:end]
        new_shape = new_family.shape
        print(f'My new shape is :{new_shape}')
        return new_family.tolist()
    except AssertionError as e:
        print(f"Assertion error : {e}")
        sys.exit(1)