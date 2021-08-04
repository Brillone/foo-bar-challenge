def init_distances_matrix(maze):
    distances_matrix = []

    for r_ix in range(len(maze)):
        distances_matrix.append([])
        for _ in range(len(maze[0])):
            distances_matrix[r_ix].append(float('inf'))

    return distances_matrix


def get_node_neighborhood(node, maze):
    neighborhood = []

    # up
    neighborhood.append((node[0]-1, node[1]))

    # left
    neighborhood.append((node[0], node[1]-1))

    # down
    neighborhood.append((node[0]+1, node[1]))

    # right
    neighborhood.append((node[0], node[1]+1))

    filtered_neighborhood = [neighbor for neighbor in neighborhood if is_legal_node(neighbor, maze)]

    return filtered_neighborhood


def is_legal_node(node, maze):
    maze_max_row = len(maze) - 1
    maze_max_col = len(maze[0]) - 1

    is_legal = node[0] >= 0 and node[0] <= maze_max_row and node[1] >= 0 and node[1] <= maze_max_col

    return is_legal


def is_node_a_wall(node, maze):
    return maze[node[0]][node[1]] == 1


def bfs(maze, source):
    distances_matrix = init_distances_matrix(maze)

    # init source
    node_to_search = [source]
    current_distance = 1
    distances_matrix[source[0]][source[1]] = current_distance

    # init bfs nextr levels
    current_distance = current_distance + 1
    next_level_nodes = []

    while len(node_to_search) > 0:
        node = node_to_search.pop()

        neighborhood = get_node_neighborhood(node, maze)

        for neighbor in neighborhood:
            if distances_matrix[neighbor[0]][neighbor[1]] == float('inf'):
                # update distance
                distances_matrix[neighbor[0]][neighbor[1]] = current_distance

                # when not a wall add to next level to check
                if not is_node_a_wall(neighbor, maze):
                    next_level_nodes.append(neighbor)
        
        if len(node_to_search) == 0:
            # increase distance as level is finished
            current_distance = current_distance + 1

            # next level to search
            node_to_search.extend(next_level_nodes)

            # reset next level
            next_level_nodes = []
    
    return distances_matrix


def solution(map):
    height = len(map)
    width = len(map[0])
    source = (height-1, width-1)
    target = (0, 0)

    # source and target distances matrixs
    distances_from_source = bfs(map, source)
    distances_from_target = bfs(map, target)

    # distance to beat
    shortest_path_distance = float('inf')

    # get both way intersects to find min distance
    for row in range(height):
        for col in range(width):
            shortest_path_distance = min(shortest_path_distance, distances_from_source[row][col] + distances_from_target[row][col]-1)

    return shortest_path_distance


# inp1 = [
#     [0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0], 
#     [0, 1, 0, 1, 0, 1, 0, 1, 0], 
#     [0, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 0],  
#     [0, 1, 0, 1, 0, 1, 0, 1, 0], 
#     [0, 1, 0, 1, 0, 1, 0, 1, 0], 
#     [0, 1, 0, 1, 0, 0, 0, 1, 0]
# ] ok

# inp2 = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 1, 1, 1, 1, 1, 1, 1, 1], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1],  
#     [1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0], 
#     [0, 1, 1, 1, 1, 1, 1, 1, 1], 
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# inp3 = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0], 
#     [0, 0, 0, 0, 0, 1, 0, 0, 0], 
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 1, 1, 1, 0, 0, 0, 0], 
#     [0, 1, 0, 1, 1, 0, 1, 1, 1], 
#     [1, 0, 0, 0, 1, 0, 0, 0, 0]
# ] ok

# inp4 = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]


if __name__ == "__main__":
    assert solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
    assert solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])) == 11
