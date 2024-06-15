import sys

def building(arg):
    """
    This function takes a string and calculate the number of digits, lower case, upper case and spaces / punctuations. 
    """
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
            elif (int(arg[i]) >= 0 and int(arg[i]) <= 9):
                digits += 1
        print(f"The text contains {l} characters:\n{upper} upper letters\n{lower} lower letters\n{punc} punctuation marks\n{space} spaces\n{digits} digits")

def main():
    """
    This main validates the argument passed to the program, it checks the length of the argument lines and its type. 
    """
        try:
            arg = sys.argv
            l = len(arg)
            if(l == 1):
                arg = input("What is the text to count?\n")
                assert (arg != "None" and arg != ""), "None or empty string entered"
                building(arg)
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