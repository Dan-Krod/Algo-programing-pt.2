def create_possible_moves():
    return [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]


def check_is_safe(x, y, board, n):
    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
        return True
    return False


def count_unvisited_neighbors(x, y, n, board):
    moves = create_possible_moves()
    return sum(1 for dx, dy in moves if check_is_safe(x + dx, y + dy, board, n))


def get_possibile_ways(x, y, board, n):
    moves = create_possible_moves()
    possibily_ways = []
    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy
        if check_is_safe(new_x, new_y, board, n):
            possibily_ways.append((new_x, new_y))
    return sorted(
        possibily_ways, key=lambda pos: count_unvisited_neighbors(*pos, n, board)
    )


def find_min_knight_pass(n, start, destination):
    if n == 2:
        return -1

    chess_board = [[0 for _ in range(n)] for _ in range(n)]
    x, y = start
    dest_x, dest_y = destination
    chess_board[x][y] = 1
    queue = [(x, y)]
    path = {(x, y): [(x, y)]}

    while queue:
        current_x, current_y = queue.pop(0)
        if current_x == dest_x and current_y == dest_y:
            shortest_path = path[(current_x, current_y)]
            return len(shortest_path) - 1
        pos = get_possibile_ways(current_x, current_y, chess_board, n)
        for next_x, next_y in pos:
            if (
                next_x,
                next_y,
            ) not in path:  # or len(path[(current_x, current_y)]) + 1 < len(path[(next_x, next_y)])
                path[(next_x, next_y)] = path[(current_x, current_y)] + [
                    (next_x, next_y)
                ]
                queue.append((next_x, next_y))

    queue.sort(key=lambda x: x[0])
    return -1


def get_min_distance_of_chess_horse(input_file_name, output_file_name):
    try:
        with open(input_file_name, "r") as file:
            board_size = int(file.readline())
            start_pos = tuple(map(int, file.readline().strip()[1:-1].split(", ")))
            end_pos = tuple(map(int, file.readline().strip()[1:-1].split(", ")))
            file.close()
    except ValueError:
        with open(output_file_name, "w") as file:
            file.write("-1")
        return

    result = find_min_knight_pass(board_size, start_pos, end_pos)

    with open(output_file_name, "w") as file:
        file.write(str(result) + "\n")
        file.close()


# n = 8
# start = (7, 0)
# destination = (0, 7)
# result = find_min_knight_pass(n, start, destination)
# print(result)
