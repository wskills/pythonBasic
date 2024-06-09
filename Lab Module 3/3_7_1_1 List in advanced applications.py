# EXAMPLE 1 - list filled with squares of ten integer numbers
squares = [x**2 for x in range(10)]
print ("squares : ",squares)

# EXAMPLE 2 -  first eight powers of two
twos = [2**i for i in range(8)]
print("twos : ",twos)

# EXAMPLE 3 -  list with only the odd elements of the squares list
odds = [x for x in squares if x % 2 != 0 ]
print("odds : ",odds)

