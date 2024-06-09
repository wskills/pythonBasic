secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

enter_number = int(input("Please enter a number :"))

while enter_number != secret_number:
    print("Ha ha! You're stuck in my loop")
    enter_number = int(input("Please enter a number :"))
print("Well done, muggle, You are free now")
    