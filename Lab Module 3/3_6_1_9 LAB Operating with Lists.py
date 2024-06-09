my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#
temp_list = []
found = True

for i in my_list:
    if i in my_list:
        del my_list[i]
        temp_list.append(i)

# my_list = temp_list[:]

print("The list with unique elements only:")
print(my_list)
