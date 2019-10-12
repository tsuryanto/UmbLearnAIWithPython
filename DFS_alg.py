def depth_first_search(graph, root):
    stack, path = [root], []
    while stack:
        vertex = stack.pop()
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

def main():
    graph={
        'Arad': ['Zerind','Timisoara', 'Sibiu'],
         'Zerind': ['Craiova','Oradea'],
        'Timisoara': ['Lugoj'],
        'Sibiu':['Rimnicu Vilcea', 'Fagaras'],
        'Oradea':[],
        'Craiova' :[],
        'Lugoj':[], 
        'Rimnicu Vilcea':[],
        'Fagaras': []
    }

    route = depth_first_search(graph, 'Arad')
    print(route)

if __name__ == '__main__':
    main();