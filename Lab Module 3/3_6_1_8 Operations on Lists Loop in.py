# EXAMPLE 1 - find the location of a given element inside a list
# Note:
# the target value is stored in the to_find variable;
# the current status of the search is stored in the found variable (True/False)
# when found becomes True, the for loop is exited.


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 11
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
     print("Element found at index", i)
else:
    print("absent")

#  EXAMPLE 2 - The question is: how many numbers have you hit?
# Note:
# the drawn list stores all the drawn numbers;
# the bets list stores your bets;
# the hits variable counts your hits.

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
