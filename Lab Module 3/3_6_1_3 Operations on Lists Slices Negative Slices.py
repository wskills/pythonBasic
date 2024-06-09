# This is how negative indices work with the slice:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

# start specifies an element lying further than the one described by the end
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
