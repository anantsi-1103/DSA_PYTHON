import heapq as h

# heap =[]


# h.heappush(heap,10)
# h.heappush(heap,30)
# h.heappush(heap,20)
# h.heappush(heap,5)

# print(heap)
# # smallest point se automatically chaltha hai

# smallest = h.heappop(heap)

# print("removed : ", smallest)
# print(heap)

# print(heap[0])


# arr = [40,10,30,50,20]

# # list ko heap m convert krna ho -> 

# h.heapify(arr)

# print(arr)


# arr = [5,4,3,1,2]
# h.heapify(arr)
# # 1 2 3 4 5

# print(arr)

# sortedArr = []

# while arr:
#    sortedArr.append(h.heappop(arr))


# print(sortedArr)
    
heap = []

h.heappush(heap, -30)
h.heappush(heap, -10)
h.heappush(heap, -15)
h.heappush(heap, -20)


print(-h.heappop(heap))