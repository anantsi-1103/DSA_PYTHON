import heapq

graph={
    0: [(1,2),(3,6)],
    1: [(0,2),(2,3),(3,8),(4,5)],
    2:[(1,3),(4,7)],
    3:[(0,6),(1,8)],
    4:[(1,5), (2,7)]
}

def prims(start):
    visited = set()


    min_heap = [(0, start)]

    total_cost = 0

    # 1 2 3 
    mst_edges = []

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        total_cost+=weight


        if weight != 0:
            mst_edges.append((node,weight))

        for neighbour , edge_weight in graph[node]:
            if neighbour not in visited:

                heapq.heappush(min_heap,(edge_weight,neighbour))

    print("MST Edges : ")
    for edge in mst_edges:
        print(edge)


    print("Total Mst Cost : ", total_cost)


prims(0)