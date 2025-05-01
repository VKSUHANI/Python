#Two arrays are the same if the elements of one array are squares of elements
#  of other arrays and regardless of the order. Consider two arrays a and b.

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False
    for x in array1:
        if x**2 in array2:
            array2.remove(x**2)
        else:
            return False
    return True
print(comp([1,2,3,4], [1,4,9,1615]) )