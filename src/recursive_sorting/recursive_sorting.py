# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print("A", arrA)
    print("B", arrB)
    #[4,3] right = [2,1]
    #merge(merge_sort[4,3],merge_sort[2,1] )
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    #merged_arr = [0,0,0,0]

    # Your code here
    #[3,7,4] [4,5]
    i = 0
    j = 0
    while  i < len(arrA) and j < len(arrB): #i=0, j=0
       

        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i]) # [3], i=1, j=0
            i = i + 1 # 2
        else:
            merged_arr.append(arrB[j]) #[0], j=1, [0,1], j=2
            j = j + 1 #1
   
    while i < len(arrA):
            
            merged_arr.append(arrA[i])
            i = i+1
    while j < len(arrB):
            merged_arr.append(arrB[j])
            j = j+1
            
    return merged_arr

# print(merge([3,7,4],[4,5]))



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # [4, 3, 2, 1]
    # base case:
    if len(arr) <= 1:
        return arr
    else: 
       
        mid = len(arr)//2
        
        #[4,3] right = [2,1]
        left = arr[:mid]
        right = arr[mid:]
        return merge(merge_sort(left),merge_sort(right))


    return arr
print(merge_sort([4,3,2,1,0]))

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    return arr
def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
