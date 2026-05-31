graph = {
    0 : [(1,5), (2,8)],
    1: [(0,5), (2,9), (3,2)],
    2: [(0,8),(1,9),(3,6)],
    3: [(1,2), (2,6)]
}

def dijkstra(start):

    # store the shortest distance
    dist = {node : float('inf') for node in graph}

    dist[start] = 0

    s = set()

    s.add((0, start))

    while s:
        curr_dist , curr_node = min(s)
        s.remove((curr_dist , curr_node))

        for neighbour , weight in graph[curr_node]:
            newDist = curr_dist + weight

            if newDist < dist[neighbour]:

                #  remove the old value 
                if dist[neighbour] != float('inf'):
                    s.discard((dist[neighbour] , neighbour))

                dist[neighbour] = newDist

                s.add((newDist,neighbour))

    return dist
            

print(dijkstra(0))

