def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    sum = 0
    if A < 0:
        for i in range(B):
                if i == abs(A-1):
                    sum += i
    else: 
        for i in range(B):        
            if i >= A:
                sum += i
    return sum

x = main(3, 6)
print(x)