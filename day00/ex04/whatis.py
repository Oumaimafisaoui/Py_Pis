import sys


def whatis():
    try:
        num1 = sys.argv[1]
        assert len(sys.argv) == 2 and num1.isnumeric(), "Invalid Argument"
        num1 = int(num1)
        print("I am even" if num1 % 2 == 0 else "I am odd")
    except AssertionError as msg: 
         print(msg)

whatis()