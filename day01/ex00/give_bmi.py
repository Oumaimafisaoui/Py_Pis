import numpy as np
import sys

def give_bmi(height:list[int| float] , weight: list[int | float]) -> list[int | float]:
    try:     
        height_np = np.array(height)
        weight_np = np.array(weight)
        assert (np.issubdtype(height_np.dtype, np.integer) or np.issubdtype(height_np.dtype, np.floating)), "Height array is not int or float"
        assert (np.issubdtype(weight_np.dtype, np.integer) or np.issubdtype(weight_np.dtype, np.floating)), "Weight array is not int or float"
        bmi = weight_np / (height_np ** 2)
        return bmi.tolist()
    except AssertionError as e:
        print(f"Assertion error: {e}")
        sys.exit(1)




def apply_limit(bmi: list[int | float], limit: list[int | float]) -> list[bool]:
    try:
        assert  isinstance(limit, int) or  isinstance(limit, float), "Limit has wrong type"
        result_compare  = np.array(bmi) < limit
        result = result_compare.tolist()
        return result
    except AssertionError as e:
        print(f"Assertion error: {e}")
        sys.exit(1)

def main():
    bmi = give_bmi([22,33,44], [55,66,77,88])
    print(apply_limit(bmi), 33)


if __name__ == "__main__":
    main()
