import numpy as np


# update/add code below ...
"""
Return all possible ways to make n pairs using a combination of pennies and nickels.
"""
def ways(n):
    result = []

    for nickels in range(n // 5 + 1):
        pennies = n - (nickels * 5)
        result.append((pennies, nickels))

    return result

print("ways 12: ", ways(12))
print("ways 20: ", ways(20))
print("ways 3: ", ways(3))
print("ways 0: ", ways(0))

def lowest_score(names, scores):
    return None

def sort_names(names, scores):
    return None
