
def quick_Sort(arr, si , ei):
    if(si < ei):

        # pivot nikal kr apke list m aage piche number swap kre 
        p = partition(arr,si,ei)

        # left - pivot ke phele number k liye wohi pivot wala logic dubara run jkro
        quick_Sort(arr,si,p-1)

        # right - pivot ke baad number k liye wohi pivot wala logic dubara run kro
        quick_Sort(arr,p+1, ei)

def partition(arr,si,ei):
    pivot = arr[ei] # last element as a pivot
    i = si - 1 # smaller element index

    for j in range(si, ei):
        if(arr[j] < pivot):
            i+=1
            arr[i],arr[j] = arr[j],arr[i] # single line swapping

    # place the pivot at the correct position
    arr[i+1], arr[ei] = arr[ei] , arr[i+1]

    return i + 1

arr = [6,3,9,8,2,5]


print("Before Sort : ", arr)
quick_Sort(arr,0,len(arr)-1)
print("After Sort : ", arr)

