# Breadth First Search implemented in python

def bfs(graph, start_node, search_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        if current_node == search_node:
            print(f"Found {search_node} in graph...")
            return
        else:
            for vertex in graph[current_node]:
                if vertex not in visited:
                    visited.append(vertex)
                    queue.append(vertex)

    print(f"{search_node} not in graph...")


def bfs_run(graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    # while queue is not empty
    while queue:
        current_node = queue.pop(0)

        for vertex in graph[current_node]:
            if vertex not in visited:
                visited.append(vertex)
                queue.append(vertex)

    # all of the vertext visited
    print(visited)


def main():
    graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []
    }

    bfs_run(graph, 'A')
    bfs(graph, 'A', 'F')
    bfs(graph, 'A', 'Z')



if __name__ == '__main__':
    main()
