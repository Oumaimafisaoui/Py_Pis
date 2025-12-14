import sys

"""
This is  a function that counts the different types of characters
in the argv[1]
"""


def count_everything(string):
    upper = lower = num = punc = space = 0
    print(f"{len(string)}")
    for char in string:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isnumeric():
             num += 1
        if char.isspace():
            space += 1
        if not char.isspace() and not char.isnumeric() and not char.isalpha():
            punc += 1
    return (f"The text contains {len(string)} characters:\n{upper} upper letters\n{lower} lower letters\n{punc} punctuation marks\n{space} spaces\n{num} digits") 
        

def handle_one(string):
    """Ctrl D works only when input() is waiting for an input"""
    try:
        print("What is the text to count?\n")
        user = sys.stdin.readline()
        if user == "":
            return
        print(count_everything(user))
    except AssertionError as e:
        print(e)


def main():
    try:
        assert len(sys.argv) <= 2, "A lot of arguments"
        args = sys.argv
        if len(args) == 1:
            handle_one(args[0])
        elif len(args) == 2:
            print(count_everything(args[1]))
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()