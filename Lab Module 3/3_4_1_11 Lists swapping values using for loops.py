# swap the list's elements to reverse their order:
# EXAMPLE 1
# my_list = [10, 1, 8, 3, 5]
# print("Original list : " , my_list)

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print("New list : ",my_list)

# EXAMPLE 2
my_list = [10, 1, 8, 3, 5]
print("Original list : " , my_list)

length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("New list : ",my_list)