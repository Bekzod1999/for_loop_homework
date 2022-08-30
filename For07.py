def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    sum = 0
    for i in range(N):
        if i%2:
            sum += i
    return sum

x=main(12)
print(x)