def check_name(name):
    if name == "l" or name == "O" or name == "I":
        print("Never use the characters 'l', 'O',"
              " or 'I' as single-character variable names")
    elif name.islower():
        print("It is a common variable")
    elif name.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
