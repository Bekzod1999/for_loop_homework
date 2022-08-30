def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list1 = ' '
    list = []
    for i in range(n):
        # list.append(i)
        if i == 0:
            list1 += str(i)
        else:
            list1 += ','+ str(i)
    return str(list1)

x = main(3)
print(x)