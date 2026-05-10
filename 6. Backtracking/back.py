def backtrack(n):
    if n > 10:
        return 
    
    print(n, end=" ")
    backtrack(n+1)

    print("Backtrack")
    # backtrack
    print(n-2, end=" ")



backtrack(1)
