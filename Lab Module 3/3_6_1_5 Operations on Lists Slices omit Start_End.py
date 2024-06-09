# If you omit the start in your slice, 
# it is assumed that you want to get a slice beginning at the element with index 0.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)


# if you omit the end in your slice, 
# it is assumed that you want the slice to end at the element with the index len(my_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
