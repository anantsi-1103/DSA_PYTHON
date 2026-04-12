def bubbleSort(list):
    n = len(list)
    for i in range(0 , n):
        for j in range(0, n-i-1):
            if list[j] < list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


def selectionSort(list):
    n = len(list)

    for i in range(0, n): # 0
        min = i
        # 5 4 3 [1] 2 = 3 
        for j in range(i+1 , n): #to find the minimum value 
            if list[j] < list[min]:
                min = j
        
        temp = list[min]
        list[min] = list[i]
        list[i] = temp


def insertionSort(list):
    n = len(list)

    for i in range(1,n):
        key = list[i]
        j = i-1

        while j>=0 and list[j]>key:
            list[j+1] = list[j]
            j = j-1
            
        list[j+1] = key

    return list


list = [5,4,3,1,2]


print("Before Sorted")
print(list)

selectionSort(list)

print("After Sorted")
print(list)
