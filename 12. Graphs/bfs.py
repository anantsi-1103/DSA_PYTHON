from collections import deque

# graph={
#     0:[1,2],
#     1:[3,4],
#     2:[],
#     3:[],
#     4:[]
# }

graph = {
 0 : [3],
1: [2,4],
2: [1],
3: [0,1],
4: [1]
}

# set 

# 1 2 3 4 
def bfs(start):
    visited = set()
    queue = deque([start])
    # 0 1 2

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)


bfs(0)