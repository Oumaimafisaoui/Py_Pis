import math

#types checks blocks errors
def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: nan <class 'float'>")
    elif isinstance(object, str) and object.strip() == '':
        print("Empty: <class 'str'>")
    elif isinstance(object, bool) and not object:
        print("Fake: False <class 'bool'>")
    elif isinstance(object, int) and object == 0: 
        print("Zero: 0 <class 'int'>")
    else:
        print("Type not Found")
        return 1
    return 0