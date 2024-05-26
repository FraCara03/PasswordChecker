def check(response):
    if response.isdigit():
        result = int(response)
        if result >= 202:
            print(result)
        else:
            print("There are less than 202 apples! You cheated me!")
    else:
        print("It is not a number!")