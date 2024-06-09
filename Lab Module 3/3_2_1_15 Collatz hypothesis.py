user_input = int(input("Please enter a number : "))
counter = 0

while user_input > 1:
    if user_input % 2 == 0:
        user_input = round(user_input / 2)
        counter += 1
        print(user_input)
    else:
        user_input = (user_input * 3)+1
        counter += 1
        print(user_input)
print("steps = ",counter)