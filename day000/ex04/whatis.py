import sys

argu = sys.argv
try:
    assert len(argu) == 2, "more than one argument is provided"
    assert argu[1].isdigit() , "argument is not an integer"
    if int(argu[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(e)