import numpy as np


def give_bmi(height:list[int| float] , weight: list[int | float]) -> list[int | float]:
    height_np = np.array(height)
    weight_np = np.array(weight)
    bmi = weight_np / (height_np ** 2)
    return bmi.tolist()




def apply_limit(bmi: list[int | float], limit: list[int | float]) -> list[bool]:
    result_compare  = np.array(bmi) < limit
    result = result_compare.tolist()
    return result

def main():
    pass


if __name__ == "__main__":
    main()
