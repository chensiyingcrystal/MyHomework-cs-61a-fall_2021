HW_SOURCE_FILE = __file__

"""Q2: Summation"""
def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!"""
    if n == 0:
        return 0
    else:
        return term(n) + summation(n - 1, term)

# print(summation(5, lambda x: x * x * x)) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
# #     225
# print(summation(9, lambda x: x + 1)) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# #     54
# print(summation(5, lambda x: 2**x)) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
# #     62


"""Q3: Pascal's Triangle"""
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle 
    whose position is specified by row and column."""
    if row == 0 and column == 0:
        return 1
    elif row == 0 and column > 0:
        return 0
    elif column == 0:
        return 1
    else:
        return pascal(row - 1, column) + pascal(row - 1, column - 1)

# print(pascal(0, 0))
# #     1
# print(pascal(0, 5))	# Empty entry; outside of Pascal's Triangle
# #     0
# print(pascal(3, 2))	# Row 3 (1 3 3 1), Column 2
# #     3
# print(pascal(4, 2))     # Row 4 (1 4 6 4 1), Column 2
# #     6


"""Q4: Insect Combinatorics"""
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner."""
    if m == 1 or n == 1:
        return 1
    else:
        return paths(m, n - 1) + paths(m - 1, n)


# print(paths(2, 2))
# #     2
# print(paths(5, 7))
# #     210
# print(paths(117, 1))
# #     1
# print(paths(1, 157))
# #     1


"""Q5: Couple"""
def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]]."""
    return [[s[i], t[i]] for i in range(0, len(s))]

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(couple(a, b))
# # [[1, 4], [2, 5], [3, 6]]
# c = ['c', 6]
# d = ['s', '1']
# print(couple(c, d))
# # [['c', 's'], [6, '1']]


"""Q6: Coordinates"""
def coords(fn, seq, lower, upper):
    return [[n, fn(n)] for n in seq if fn(n) <= upper and fn(n) >= lower]


# seq = [-4, -2, 0, 1, 3]
# fn = lambda x: x**2
# print(coords(fn, seq, 1, 9))
# # [[-2, 4], [1, 1], [3, 9]]


"""Q7: Riffle Shuffle"""
def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even."""
    return [deck[(len(deck) - i) // 2 + i] if i % 2 != 0 else deck[i // 2] for i in range(0, len(deck))]

print(riffle([3, 4, 5, 6]))
    # [3, 5, 4, 6]
print(riffle(range(20)))
    # [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
# print([i for i in range(20)])

# i = 0 deck[0]
# i = 1 deck[(len(deck) - 1) // 2 + 1]
# i = 2 deck[1]
# i = 3 deck[(len(deck) - 3) // 2 + 3]