def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    list=[]
    for i in range(11):
        if i > 0:
            list.append(i*price)
    return list

x=main(2.25)
print(x)