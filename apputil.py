import numpy as np


# update/add code below ...

def ways(n):
    final = []
    count = (n/5)+1
    i = 1

    while i<=count:
        remainder = n%i
        final.append(remainder, i)
    
    return final

ways(12)

# def lowest_score(names, scores):
#     return None

# def sort_names(names, scores):
#     return None