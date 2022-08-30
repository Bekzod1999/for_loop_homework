def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list = []
    for i in range(n):
        i = k
        list.append(i)
    return list

x = main(-1, 3)
print(x)
