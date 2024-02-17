# Floyd-s_Algorithm
For mid module assignment 
# Floyd's Algorithm Implementation

This project implements Floyd's algorithm for finding the shortest paths between all pairs of vertices in a graph. It includes both iterative and recursive implementations of the algorithm.
# Installation

To use this project, you need to have Python installed on your system. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/floyds-algorithm.git

Navigate to the project directory:
cd floyds-algorithm

Install the dependencies:
pip install -r requirements.txt

## Usage
You can use both the iterative and recursive implementations of Floyd's algorithm by importing the corresponding functions from floyds_algorithm module.

Example usage:
from floyds_algorithm import floyd, floyd_recursive

# Create a graph (adjacency matrix)
graph1 = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]

# Use the iterative implementation
shortest_paths_iterative = floyd(graph)

# Use the recursive implementation
shortest_paths_recursive = floyd_recursive(graph)

## Running Tests
To run unit tests, execute the following command:

pytest

To run performance tests, execute:

pytest --benchmark-autosave

## Performance Comparison
After running the performance tests, you can compare the performance of the iterative and recursive implementations.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

In this README file:

- Installation instructions guide users on how to clone the repository, install dependencies, and set up the project.
- Usage section demonstrates how to use the implemented functions in Python code.
- Running Tests section explains how to run unit tests and performance tests using pytest.
- Performance Comparison section encourages users to compare the performance of the iterative and recursive implementations after running the performance tests.
- License section provides information about the project's license.
