import numpy as np


# update/add code below ...

#Q1
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



#Q2.

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

#Part - 1

def lowest_score(names, scores):

"""
Return the name of the student with the lowest test score.
"""
    
    return names[np.argmin(scores)]

#Part - 2

def sort_names(names, scores):
"""
Return names sorted in descending order of test score.
"""
    return names[np.argsort(scores)[::-1]]

#test output
print("Student with lowest score:")
print(lowest_score(names, scores))

print("\nStudents sorted by score (highest to lowest):")
sorted_names = sort_names(names, scores)
for name in sorted_names:
    print(name)
