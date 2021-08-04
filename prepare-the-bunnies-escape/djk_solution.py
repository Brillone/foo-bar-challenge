def init_distances_info_matrix(maze):
    distances_matrix = []

    for r_ix in range(len(maze)):
        distances_matrix.append([])
        for _ in range(len(maze[0])):
            distances_matrix[r_ix].append({'distance': float('inf'), 'is_wall_removed': False})

    return distances_matrix


def get_min_distance_node(distances_info_matrix, done_nodes):
    min_distance = float('inf')
    min_row_col = (-1, -1)

    for r_ix in range(len(distances_info_matrix)):
        for c_ix in range(len(distances_info_matrix[0])):
            if (r_ix, c_ix) in done_nodes:
                continue
            if distances_info_matrix[r_ix][c_ix]['distance'] < min_distance:
                min_distance = distances_info_matrix[r_ix][c_ix]['distance']
                min_row_col = (r_ix, c_ix)

    return min_row_col, distances_info_matrix[min_row_col[0]][min_row_col[1]]


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


def check_node_is_a_wall(node, maze):
    return maze[node[0]][node[1]] == 1


def search_shortest_path(maze, source, target, break_walls=False, distances_info_matrix_no_break=None):
    distances_info_matrix = init_distances_info_matrix(maze)
    done_nodes = []

    # init start
    distances_info_matrix[source[0]][source[1]]['distance'] = 1
    distances_info_matrix[source[0]][source[1]]['is_wall_removed'] = False

    while len(done_nodes) < len(maze)*len(maze[0]):
        current_node, current_node_distance_info = get_min_distance_node(distances_info_matrix, done_nodes)

        if current_node == (-1, -1):
            break

        for neighbor in get_node_neighborhood(current_node, maze):  
            if neighbor in done_nodes:
                continue
            
            # current node info
            current_node_distance = current_node_distance_info['distance']
            current_node_is_wall_removed = current_node_distance_info['is_wall_removed']

            # current neighbor distance info 
            neighbor_current_distance = distances_info_matrix[neighbor[0]][neighbor[1]]['distance']
            neighbor_current_is_wall_removed = distances_info_matrix[neighbor[0]][neighbor[1]]['is_wall_removed']
            is_neighbor_wall = check_node_is_a_wall(neighbor, maze)
            
            if (not break_walls) and is_neighbor_wall:
                continue
            elif break_walls and current_node_is_wall_removed and is_neighbor_wall and not check_node_is_a_wall(current_node, maze):
                if distances_info_matrix_no_break[current_node[0]][current_node[1]]['distance'] != float('inf'):
                    current_node_distance_info = distances_info_matrix_no_break[current_node[0]][current_node[1]]
                    
                    # distances_info_matrix[current_node[0]][current_node[1]] = current_node_distance_info
                    current_node_distance = current_node_distance_info['distance']
                    current_node_is_wall_removed = current_node_distance_info['is_wall_removed']
            
            if current_node_is_wall_removed and is_neighbor_wall:
                continue

            # new neighbor distance info
            neighbor_new_distance = current_node_distance + 1
            neighbor_new_is_wall_removed = is_neighbor_wall or current_node_is_wall_removed
            
            if neighbor_new_distance < neighbor_current_distance:
                distances_info_matrix[neighbor[0]][neighbor[1]]['distance'] = neighbor_new_distance
                distances_info_matrix[neighbor[0]][neighbor[1]]['is_wall_removed'] = neighbor_new_is_wall_removed
                distances_info_matrix[neighbor[0]][neighbor[1]]['prev'] = current_node
            elif neighbor_new_distance == neighbor_current_distance:
                if (neighbor_current_is_wall_removed) and (not neighbor_new_is_wall_removed):
                    distances_info_matrix[neighbor[0]][neighbor[1]]['is_wall_removed'] = neighbor_new_is_wall_removed
                    distances_info_matrix[neighbor[0]][neighbor[1]]['prev'] = current_node
                    
        done_nodes.append(current_node)

    return distances_info_matrix


def solution(map):
    height = len(map)
    width = len(map[0])
    source = (height-1, width-1)
    target = (0, 0)

    distances_info_matrix = search_shortest_path(map, source, target, break_walls=False, distances_info_matrix_no_break=None)
    distances_info_matrix = search_shortest_path(map, source, target, break_walls=True, distances_info_matrix_no_break=distances_info_matrix)
    shortest_path_distance = distances_info_matrix[target[0]][target[1]]['distance']

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
    """
    Not passing all test cases. Not a good solution.
    """
    assert solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
    assert solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])) == 11
