# def main(n):
#     """
#     Return numbers from zero to n in a string view.
#     Args:
#         n: int
#     Returns:
#         string: return  answer
#     """
#     list1 = ' '
#     list = [] 
#     for i in range(n):
#         # list.append(i)
#         if i == 0:
#             list1 += '"' + str(i)
#         elif i == n - 1:
#             list1 += ',' + str(i) + '"'
#         else:
#             list1 += ','+ str(i)
#     return str(list1)

# x = main(30)
# print(x)



def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    list1 = ''
    list = [] 
    m = ','
    for i in range(n):
        list.append(str(i))
        str(list)
        k = m.join(list)
    return k

x = main(3)
print(x)