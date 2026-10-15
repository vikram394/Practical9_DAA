import heapq

def prim_mst(graph, start_vertex=0):
    """
    Finds the Minimum Spanning Tree (MST) using Prim's Algorithm.
    
    :param graph: Dict representing the adjacency list {vertex: [(neighbor, weight), ...]}
    :param start_vertex: The node from which the algorithm begins
    :return: A list of tuples representing the MST edges (from, to, weight) and the total cost
    """
    visited = set()
    min_heap = [(0, start_vertex, None)]
    
    mst_edges = []
    total_cost = 0
    
    while min_heap:
        weight, current_vertex, parent = heapq.heappop(min_heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        total_cost += weight
        if parent is not None:
            mst_edges.append((parent, current_vertex, weight))
 
        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_vertex))
                
    return mst_edges, total_cost

if __name__ == "__main__":
    example_graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    
    mst, cost = prim_mst(example_graph, start_vertex=0)
    
    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"Edge: {u} - {v} | Weight: {weight}")
    print(f"\nTotal MST Cost: {cost}")
