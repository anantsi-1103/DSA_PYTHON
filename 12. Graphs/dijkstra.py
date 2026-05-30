import heapq

graph = {
    0 : [(1,5), (2,8)],
    1: [(0,5), (2,9), (3,2)],
    2: [(0,8),(1,9),(3,6)],
    3: [(1,2), (2,6)]
}

def dijkstra(start):

    # store the shortest distance
    distance = {}

    # initially infinity 
    

