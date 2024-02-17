# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:08:09 2024

@author: lenovo
"""

import pytest
from floyds_algorithm import floyd, floyd_recursive
import random

# Generate a random adjacency matrix for testing
def generate_random_graph(n):
    graph = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            elif random.random() < 0.2:  # Adjust the probability for edge creation
                graph[i][j] = random.randint(1, 100)  # Adjust the range for edge weights
    return graph

@pytest.fixture
def small_graph():
    return generate_random_graph(10)

@pytest.fixture
def large_graph():
    return generate_random_graph(100)

# Performance test for the recursive implementation
def test_floyd_recursive_performance(benchmark, small_graph):
    result = benchmark(floyd_recursive, small_graph)

# Performance test for the iterative implementation
def test_floyd_performance(benchmark, small_graph):
    result = benchmark(floyd, small_graph)

# Performance test for the recursive implementation on a larger graph
def test_floyd_recursive_performance_large(benchmark, large_graph):
    result = benchmark(floyd_recursive, large_graph)

# Performance test for the iterative implementation on a larger graph
def test_floyd_performance_large(benchmark, large_graph):
    result = benchmark(floyd, large_graph)
