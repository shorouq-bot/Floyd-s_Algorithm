# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:02:28 2024

@author: lenovo
"""
#alculates the shortest path between vertices i and j, considering the intermediate vertex k.
def floyd_recursive(graph, i, j, k):
    """
    Recursively finds the shortest path between vertices i and j considering intermediate vertex k.

    Args:
    graph: 2D array representing the graph.
    i, j, k: Vertices in the graph.

    Returns:
    The shortest path length between vertices i and j considering intermediate vertex k.
    """
    if k == 0:
        return graph[i][j]
    else:
        return min(floyd_recursive(graph, i, j, k-1), 
                   floyd_recursive(graph, i, k, k-1) + floyd_recursive(graph, k, j, k-1))
#applies Floyd's algorithm to find the shortest paths between all pairs of vertices in the given graph.
def floyd(graph):
    """
    Applies Floyd's algorithm to find the shortest paths between all pairs of vertices in a graph.

    Args:
    graph: 2D array representing the graph.

    Returns:
    A 2D array representing the shortest paths between all pairs of vertices.
    """
    n = len(graph)
    distances = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = floyd_recursive(graph, i, j, n-1)
    return distances
