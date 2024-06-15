import sys

def building(arg):
        upper = lower= digits=  punc = space = 0
        arg = arg
        l = len(arg)
        for i in range(len(arg)):
            if(arg[i] >= 'a' and arg[i] <= 'z'):
                lower += 1
            elif(arg[i] >= 'A' and arg[i] <= 'Z'):
                upper +=1
            elif(not arg[i].isalnum() and not arg[i].isspace()):
                punc += 1
            elif (arg[i].isspace()):
                space += 1
            elif (arg[i].isdigit()):
                digits += 1
        print(f"The text contains {l} characters:\n{upper} upper letters\n{lower} lower letters\n{punc} punctuation marks\n{space} spaces\n{digits} digits")

def handle_one_argument():
    """Ctrl D works only when input() is waiting for an input"""
    try:
        line = input("What is the text to count?\n")
        assert (line != "None" and line != ""), "None or empty string entered"
        building(line)
    except EOFError:
        pass
    except AssertionError as e:
        print(f"Assertion error: {e}")

def main():
        try:
            arg = sys.argv
            l = len(arg)
            if(l == 1):
                handle_one_argument()
            elif(l == 2):
                assert (arg[1] != "None" and arg[1] != ""), "None or empty string entered"
                building(arg[1])
            else:
                raise Exception("Answer only one string")
        except AssertionError as e:
            print(f"Asssertion Error : {e}")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
        
    
if __name__ == "__main__":
    main()