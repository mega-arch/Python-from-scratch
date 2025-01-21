# Check if an element is in the array
def element_in_array(arr, element): #both array and the element to be checked is given in paramater
    for i in range(len(arr)): #length of the array is set as range
        if arr[i] == element: #checks if it is there 
            return True
    return False
    
print(element_in_array([1, 2, 3, 4], 3))  # Output: True
