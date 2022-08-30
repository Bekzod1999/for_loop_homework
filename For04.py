def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list = []
    for i in range(B+1):
        if i >= A:
            list.append(i)
    return list
x=main(2, 7)
print(x)