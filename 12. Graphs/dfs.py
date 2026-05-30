# graph={
#     0:[1,2],
#     1:[3,4],
#     2:[],
#     3:[],
#     4:[]
# }

graph = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3]
}


visited = set()

def dfs(node): #0 1 3

    visited.add(node)

    print(node,end=" ") # 0. 1 3 4

    for n in graph[node]: # 2  
        if n not in visited: # 1
            dfs(n) # dfs(1)


dfs(0)