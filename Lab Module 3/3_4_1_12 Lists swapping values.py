# Imagine that you need to rearrange the elements of a list, 
# i.e., reverse the order of the elements: the first and the fifth 
# as well as the second and fourth elements will be swapped. 
# The third one will remain untouched.

variable_1 = 5
variable_2 = 7
print("Old values variable1 and variable2 : ", variable_1, variable_2)

variable_1, variable_2 = variable_2, variable_1
print("New values variable1 and variable2 : ", variable_1, variable_2)