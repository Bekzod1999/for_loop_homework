def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list1 = []
    for i in range(B+1):
        if i >= A:
            list1.append(i)
    return list1[-1::-1]

x =main(5, 9)
print(x)