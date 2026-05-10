
def merge_Sort(arr):
    if(len(arr)>1):
        mid = len(arr)//2 # find middle
        left = arr[ :mid] # by default it will take 0 - left half
        right = arr[mid: ] # by default it will take len(last index) - right half

        # recursivly call hota rhega ek ek number nhi niklenge
        merge_Sort(left)  
        merge_Sort(right)  

        i = j = k = 0

        # merge sort
        while i < len(left) and j < len(right):
            if(left[i] < right[j]):
                arr[k] = left[i] # left wali value store hogi
                i+=1
            else:
                arr[k] = right[j] # right wali value store hogi
                j+=1
            k+=1 # key increment

        # add remaining element
        while(i < len(left)):
            arr[k] = left[i]
            i+=1
            k+=1

        while(j < len(right)):
            arr[k] = right[j]
            j+=1
            k+=1

arr = [6,3,9,2,5,8]


print("Before Sort : ", arr)
merge_Sort(arr)
print("After Sort : ", arr)