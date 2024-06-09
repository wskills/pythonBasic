numbers = [10, 5, 7, 2, 1]
print("Original list : ", numbers)  # Printing original list content.

numbers[0] = 111
print("Previous list : ", numbers)

numbers[1] = numbers[4]
print("New list : ", numbers)
