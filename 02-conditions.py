try:
    user_input = int(input("Enter a number"))
    #user_input = int(user_input)

    if user_input > 10:
        print("given num is graterthan 10")
    else:
        print("given num is not lessthan or equal to 10")
except ValueError:
    print("Please enter a number")