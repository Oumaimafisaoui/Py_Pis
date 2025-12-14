import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: nan <class 'float'>")
    elif isinstance(object, bool):
        print("Fake: False <class 'bool'>")
    elif isinstance(object, int) and object == 0:
        print("Zero: 0 <class 'int'>")
    elif isinstance(object, str) and object == "":
        print("Empty: <class'str'>")
    else:
        print("Type not Found")
    return 1