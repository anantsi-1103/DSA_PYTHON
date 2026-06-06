# number of vertices
v = 4

# create matrix -> 
graph = [[0 for _ in range(v)] for _ in range(v)]

# add Edges
graph[0][1] = 1
graph[1][0] = 1

graph[0][2] = 1
graph[2][0] = 1

graph[1][3] = 1
graph[3][1] = 1

graph[2][3] = 1
graph[3][2] = 1


# print
for row in graph:
    print(row)


    # Adjanency list


