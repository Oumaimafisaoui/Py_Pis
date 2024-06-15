import sys


def filterString(arg, l):
    words = arg.split()
    return [word for word in words if len(word) == l]

def main():
    try:
        l = len(sys.argv)
        assert l == 3, "the arguments are bad"
        assert (sys.argv[1] and sys.argv[2] and sys.argv[1] != "None" and not sys.argv[1].isdigit() and sys.argv[2].isdigit() and sys.argv[2] != 0), "the arguments are bad"
        print(filterString(sys.argv[1], int(sys.argv[2])))
    except AssertionError as e:
        print(f"Assertion Error: {e}")



if __name__ == "__main__":
    main()