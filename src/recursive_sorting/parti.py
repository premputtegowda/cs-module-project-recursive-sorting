
def merge(arr, start, mid, end): 
    #merge([4,3,2,1],l=0,m=1,r=1)
    start2 = mid + 1; 
    #start = 0, start2 = 2, mid=1, end=3
 
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return; 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; # value 2 
            index = start2;  # 2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): # start = 0
                arr[index] = arr[index - 1]; # arr[2] = arr[1]
                index -= 1; 
              
            arr[start] = value; 
  
            # Update all the pointers 
            start += 1; 
            mid += 1; 
            start2 += 1; 
   
#[1, 5, 8, 4, 2, 9, 6, 0, 3, 7], 0, 9
def mergeSort(arr, l, r): 
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2; #4
  
        # Sort first and second halves 
        mergeSort(arr, l, m)
        #mergeSort([4,3,2,1], 0, 3)
            #mergeSort([4,3,2,1], 0, 1 ) # left ( didn't do anything)
                #mergeSort([4,3,2,1], 0, 0 ) # left ## not run
                #mergeSort([4,3,2,1], 1, 1 ) # right ## not run

            #mergeSort([4,3,2,1], 2, 3 ) # right
                #mergeSort([4,3,2,1], 2, 2 ) # left ## not run
                #mergeSort([4,3,2,1], 3, 3 ) # right ###  not run
                
           
        mergeSort(arr, m + 1, r); 
  
        merge(arr, l, m, r)
         #merge([4,3,2,1],l=0,m=1,r=1)

print(mergeSort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7], 0, 9))


[1, 5, 8, 4, 2, 9, 6, 0, 3, 7],0,0
                                0,1
                                0,2
[1]