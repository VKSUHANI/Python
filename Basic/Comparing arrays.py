# Two arrays are considered the same if the elements of one array are squares 
# of the elements of the other array, regardless of the order.

def comp(array1, array2):
    # Check if either of the arrays is None
    if array1 is None or array2 is None:
        return False
    
    # Check if the lengths of the arrays are different
    if len(array1) != len(array2):
        return False
    
    # Iterate through each element in the first array
    for x in array1:
        # Check if the square of the current element exists in the second array
        if x**2 in array2:
            # Remove the squared element from the second array to avoid duplicates
            array2.remove(x**2)
        else:
            # If the square is not found, the arrays are not the same
            return False
    
    # If all checks pass, the arrays are considered the same
    return True

# Test the function with example arrays
print(comp([1, 2, 3, 4], [1, 4, 9, 16]))  # Expected output: True
print(comp([1, 2, 3, 4], [1, 4, 9, 1615]))  # Expected output: False