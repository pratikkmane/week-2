import numpy as np


def ways(cents, coin_types=None):
    """Calculate the number of ways to make change for a given amount.

    Args:
        cents (int): The amount of cents to make change for.
        coin_types (list, optional): List of coin denominations to use.
            Defaults to [1, 5] (pennies and nickels).

    Returns:
        int: The number of different ways to make change for the given amount.

    Examples:
        >>> ways(12)
        3
        >>> ways(20)
        5
        >>> ways(100, [25, 10, 5, 1])
        242
    """
    if coin_types is None:
        coin_types = [1, 5]

    # Sort coin types in descending order for efficiency
    coin_types = sorted(coin_types, reverse=True)

    # Dynamic programming approach
    # dp[i] represents the number of ways to make change for i cents
    dp = [0] * (cents + 1)
    dp[0] = 1  # One way to make 0 cents: use no coins

    # For each coin type
    for coin in reversed(coin_types):
        # Update the number of ways for each amount
        for amount in range(coin, cents + 1):
            dp[amount] += dp[amount - coin]

    return dp[cents]


def ways_simple(n):
    """Calculate ways to make change using only pennies (1) and nickels (5).

    This is a simplified version specifically for pennies and nickels.

    Args:
        n (int): The amount of cents to make change for.

    Returns:
        int: The number of different ways to make change.

    Examples:
        >>> ways_simple(12)
        3
        >>> ways_simple(20)
        5
        >>> ways_simple(3)
        1
        >>> ways_simple(0)
        1
    """
    # For pennies and nickels, we can use a mathematical approach:
    # For any amount n, the number of ways is (n // 5) + 1
    # This is because we can use 0, 1, 2, ... n//5 nickels,
    # and fill the rest with pennies
    return (n // 5) + 1


# Exercise 2: Student Scores Functions

def lowest_score(names, scores):
    """Return the name of the student with the lowest score.

    Args:
        names (np.ndarray): Array of student names.
        scores (np.ndarray): Array of corresponding test scores.

    Returns:
        str: The name of the student with the lowest score.

    Examples:
        >>> names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
        >>> scores = np.array([99, 71, 85, 62, 91])
        >>> lowest_score(names, scores)
        'Mauve'
    """
    # Finding the index of the minimum score
    min_index = np.argmin(scores)
    # Returning the name at that index
    return names[min_index]


def sort_names(names, scores):
    """Return student names in descending order of test scores.

    Args:
        names (np.ndarray): Array of student names.
        scores (np.ndarray): Array of corresponding test scores.

    Returns:
        np.ndarray: Array of student names sorted by scores (highest to
            lowest).

    Examples:
        >>> names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
        >>> scores = np.array([99, 71, 85, 62, 91])
        >>> sort_names(names, scores)
        array(['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve'], dtype='<U6')
    """
    # Getting indices that would sort scores in descending order
    # argsort() sorts in ascending order, so we use [::-1] to reverse
    sorted_indices = np.argsort(scores)[::-1]
    # Return names in the sorted order
    return names[sorted_indices]


if __name__ == "__main__":
    # Test cases for basic function
    print("Testing ways() function:")
    print(f"ways(12) = {ways(12)} (expected: 3)")
    print(f"ways(20) = {ways(20)} (expected: 5)")
    print(f"ways(3) = {ways(3)} (expected: 1)")
    print(f"ways(0) = {ways(0)} (expected: 1)")

    print("\nTesting optional variation:")
    print(f"ways(100, [25, 10, 5, 1]) = {ways(100, [25, 10, 5, 1])} "
          f"(expected: 242)")

    print("\nTesting simple version:")
    print(f"ways_simple(12) = {ways_simple(12)} (expected: 3)")
    print(f"ways_simple(20) = {ways_simple(20)} (expected: 5)")

    # Test cases for Exercise 2
    print("\n" + "=" * 50)
    print("Testing Exercise 2: Student Scores Functions")
    print("=" * 50)

    names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
    scores = np.array([99, 71, 85, 62, 91])

    print("\nTest data:")
    print(f"Names:  {names}")
    print(f"Scores: {scores}")

    print("\nTesting lowest_score():")
    lowest = lowest_score(names, scores)
    print(f"Student with lowest score: {lowest} (expected: Mauve)")

    print("\nTesting sort_names():")
    sorted_names = sort_names(names, scores)
    print(f"Names in descending score order:")
    print(f"  {sorted_names}")
    print(f"  (expected: ['Hannah', 'Jung', 'Abdul', 'Astrid', 'Mauve'])")

    # Verifying the sorting by showing scores
    sorted_indices = np.argsort(scores)[::-1]
    sorted_scores = scores[sorted_indices]
    print(f"\nCorresponding scores: {sorted_scores}")
