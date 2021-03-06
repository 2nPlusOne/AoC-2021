from os import path

def main():
    with open(path.join(path.dirname(__file__), 'sample.txt')) as f:
        graph = create_graph([line.strip().split("-") for line in f.readlines()])
    f.close()
    
    part1_paths = BFS_traversals_part1(graph)
    part2_paths = BFS_traversals_part2(graph)

    print(f"Part 1: The number of paths through the cave system that visit small caves at least once is {len(part1_paths)}.")
    print(f"Part 2: The number of paths through the cave system that visit a single small cave twice and the rest once is {len(part2_paths)}.")

def create_graph(lines):
    """Creates a graph of the cave system from the input lines."""
    graph = {}
    for line in lines:
        if line[0] not in graph:
            graph[line[0]] = []
        if line[1] not in graph:
            graph[line[1]] = []
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])
    return graph

def BFS_traversals_part1(graph: dict, start='start', end='end'):
    """Returns a list of all unique paths through the cave system from start to end, visiting each small cave at most once."""
    stack = [[start]] # List of branches to explore, initialized to the start node
    paths = [] # List of paths found so far
    while stack:
        path = stack.pop(0)
        node = path[-1]
        if node == end: # Found a path to the end
            paths.append(path) # Add the path to the list of paths
            continue
        for neighbor in graph[node]:
            if neighbor in path and neighbor.islower(): continue
            stack.append(path + [neighbor]) # Add the new path branch to the stack of branches left to explore
    return paths

def BFS_traversals_part2(graph: dict, start='start', end='end'):
    """Returns a list of all unique paths through the cave system from start to end, 
       visiting a single small cave at most twice, and the rest once."""
    stack = [([start], False)] # A list of paths and whether the path has visited any single small cave twice
    paths = []
    while stack:
        path, small_revisited = stack.pop(0)
        node = path[-1]
        if node == end:
            paths.append(path)
            continue
        for neighbor in graph[node]:
            if neighbor not in path or neighbor.isupper():
                stack.append((path + [neighbor], small_revisited))
            elif not small_revisited and neighbor != start:
                stack.append((path + [neighbor], True)) # Add the path branch and mark that the path has visited a single small cave twice
    return paths


if __name__ == '__main__':
    main()