import collections

def breadth_first_search(graph, root):
    visited, queue = [], collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

def main():
    graph={
        'Arad': ['Zerind','Timisoara', 'Sibiu'],
        'Zerind': ['Oradea'],
        'Timisoara': ['Lugoj'],
        'Sibiu':['Rimnicu Vilcea', 'Fagaras'],
        'Oradea':[],
        'Lugoj':[],
        'Rimnicu Vilcea':[],
        'Fagaras': []
    }
    route = breadth_first_search(graph, 'Arad')
    print(route)

if __name__ == '__main__':
    main();