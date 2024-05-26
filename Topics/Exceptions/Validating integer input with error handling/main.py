# Get user input and handle exceptions
#integer = input()

while True:
    try:
        num = int(input())
        break
    except ValueError:
        # TODO: Handle the exception when input is not an integer
        print("Invalid input. Please enter an integer.")

# TODO: Print the square of the input integer
print(num*num)