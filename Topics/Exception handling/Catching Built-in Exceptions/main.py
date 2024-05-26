try:
    a = int(input())
    b = int(input())
    result = a / b
    print(result)
except ZeroDivisionError:
    print("The Error!")
except ValueError:
    print("Invalid input! Please enter valid integers.")