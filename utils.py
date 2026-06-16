import networkx as nx

# Outside function to map given string museum_map into actual graph.
# 'O' indicates a room in the museum, 'W' indicates a wall, example:
# custom_map = [
#     "OOOOO",
#     "OOWOO"
# ]
def map_museum_to_graph(museum_map):
    base_graph = nx.Graph()
    valid_rooms = []
    height = len(museum_map)
    width = len(museum_map[0])

    for y in range(height):
        for x in range(width):
            if museum_map[y][x] == 'O':
                valid_rooms.append((x, y))
                base_graph.add_node((x, y))

                # Connect to left neighbor if it's a room
                if x > 0 and museum_map[y][x - 1] == 'O':
                    base_graph.add_edge((x, y), (x - 1, y))
                # Connect to top neighbor if it's a room
                if y > 0 and museum_map[y - 1][x] == 'O':
                    base_graph.add_edge((x, y), (x, y - 1))

    return base_graph, len(valid_rooms)
