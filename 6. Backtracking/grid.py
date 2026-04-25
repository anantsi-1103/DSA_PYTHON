def gridways(i,j,n,m):

    # 0 == 4 , 0 == 4
    # destination reach
    if((i == n-1) and(j == m-1)):
        return 1
    
    # out of bound
    if i== n or j == m:
        # 0 likh do - purani jagah vapis aajao
        return 0
    

    
    # Move logic
    return gridways(i+1,j, n,m) + gridways(i,j+1,n,m)
#                   4,2 + 1 + 4

n = 4
m = 4

print(gridways(0,0,n,m))