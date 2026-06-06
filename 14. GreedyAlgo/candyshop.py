
def candyStore(candies , k):

    candies.sort()
    
    n = len(candies)

    # minumum cost
    min_cost = 0
    i = 0
    j = n - 1

    while i <= j:
        min_cost += candies[i]

        i+=1
        j-=k
    
    # maximum cost
    max_cost = 0
    i = 0
    j = n - 1

    while i <= j:
        max_cost += candies[j]
        j-=1
        i+=k

    return min_cost , max_cost




candies = [3, 2, 1, 4]
k = 2


print(candyStore(candies, k))