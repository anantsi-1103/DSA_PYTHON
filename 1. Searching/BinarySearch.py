# binary search m list woh apki sorted honi chaieye

list = [2,4,6,8,10,12,13,14,15,16,25,68,95]


def binarySearch(list ,key):
    si = 0
    ei = len(list)-1

    while(si <= ei):
        mid = (si + ei)//2

        if(list[mid] == key):
            return mid
        elif(list[mid] < key):
            si = mid + 1
        else:
            ei = mid - 1
    return -1

    

print(binarySearch(list,14))