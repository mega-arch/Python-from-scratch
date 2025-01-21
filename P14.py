# Merge two arrays
def merge_arrays(arr1, arr2): #2 parameters for 2 arrays to be merged 
    merged = [] #create empty array
    index = 0 #position of each element in array 
    for i in range(len(arr1)): #length of arr1 is range of iteration
        merged[index] = arr1[i] #ith elemnet of arr1 is assigned to merged array intially 0 th index has ith element of arr1
        index += 1
        
    for i in range(len(arr2)):
        merged_array[index] = arr2[i]
        index += 1

print(merge_arrays([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]

    
