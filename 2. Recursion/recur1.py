# sum of n natural -> n -> 1----n -> +

n = int(input("Enter your n value : \n"))


def sum_loop(n): # 5
    sum = 0 # 0 1 3 6 10 15
    for i in range(1, n+1):
        # 1 2 3 4 5
        sum += i
        # sum = sum + i 
        # sum = 10 + 5
    return sum


def sum_rec(n):
    # base case 
    if(n == 0):
        return n
    # kaam
    return n + sum_rec(n-1)


def fact_loop(n): # 5
    fact = 1 # 
    for i in range(1, n+1):
        fact *= i
    return fact


def fact_rec(n):
    # base case 
    if(n == 1):
        return n
    # kaam
    return n * fact_rec(n-1)

def count(n):
    if(n == 1):
        return n
    
    print(n)
    return count(n-1)

def count_asc(si, ei): 
    if(si == ei + 1): 
        return si
    
    print(si)
    return count_asc(si + 1 , ei) 




# print(count(n))
# print(fact_loop(n))
# print(fact_rec(n))
# print(sum_loop(n))
# print(sum_rec(n))