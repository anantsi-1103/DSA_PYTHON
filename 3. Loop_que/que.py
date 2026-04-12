def fibo(n):
    a = 0
    b = 1
    # print(a,b,end=" ")
    # 0 1
    c = 0
    for i in range(2, n+1):
        c = a+b
        # print(c,end=" ")
        a = b
        b = c
    print(c)
    # print()


def fibo_rec(n):
    if n == 1 or n == 0:
        return n

    return fibo_rec(n-1) + fibo_rec(n-2)

fibo(10)

print(fibo_rec(10))