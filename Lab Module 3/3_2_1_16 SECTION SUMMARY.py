## ----- while loop instructions -----

# Example 1
##while True:
##    print("Stuck in an infinite loop.")

# Example 2
##counter = 5
##while counter > 2:
##    print(counter)
##    counter -= 1

## ----- for loop instructions -----

# Example 1
##word = "Python"
##for letter in word:
##    print(letter, end="*")

### Example 2
##for i in range(1, 10):
##    if i % 2 == 0:
##        print(i)

## ----- break and continue instructions -----

##text = "OpenEDG Python Institute"
##for letter in text:
##    if letter == "P":
##        break
##    print(letter, end="")

##text = "pyxpyxpyx"
##for letter in text:
##    if letter == "x":
##        continue
##    print(letter, end="")

## ----- while and for loops with else clause -----

##n = 0
##
##while n != 3:
##    print(n)
##    n += 1
##else:
##    print(n, "else")
##
##print()
##
##for i in range(0, 3):
##    print(i)
##else:
##    print(i, "else")

## ----- range in for loops (start, stop, step)-----

##for i in range(3):
##    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -1):
    print(i, end=" ")  # Outputs: 6, 4, 2
