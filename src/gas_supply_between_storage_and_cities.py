def dfs(graph, start):
    stack = [start]
    visited_cities = []
    while stack:
        cur_city = stack.pop()
        if cur_city in visited_cities:
            continue
        visited_cities.append(cur_city)
        if cur_city in graph:
            for neighbour in graph[cur_city]:
                if neighbour not in visited_cities:
                    stack.append(neighbour)
    return visited_cities


def build_graph(cities, gas_lines):
    graph = {}
    for city in cities:
        if city not in graph:
            graph[city] = []
    for gas_line in gas_lines:
        start_city, dest_city = gas_line
        if start_city not in cities or dest_city not in cities:
            continue
        else:
            graph[start_city].append(dest_city)
    return graph


def get_unreachable_cities_for_gas_storage(storage, visited, cities):
    difference = [city for city in cities if city not in visited]
    return storage, difference


def find_and_get_unreachable_cities_supply(input_file, output_file):
    cities, storages, gas_lines = read_data_from_file(input_file)
    if not cities:
        write_data_to_file(output_file, ["-1"])
        return

    unreachable_cities = []
    graph = build_graph(cities, gas_lines)
    for storage in storages:
        if storage in cities:
            visited = dfs(graph, storage)
            info_of_cur_storage = get_unreachable_cities_for_gas_storage(
                storage, visited, cities
            )
        else:
            continue
        if len(info_of_cur_storage) != 0:
            unreachable_cities.append(str(info_of_cur_storage))
        else:
            continue

    write_data_to_file(output_file, unreachable_cities)


def read_data_from_file(input_filename):
    cities = []
    storages = []
    gas_lines = []

    with open(input_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            cities = lines[0].strip().split()
            storages = lines[1].strip().split()
            gas_lines = [line.strip().split() for line in lines[2:]]

    return cities, storages, gas_lines


def write_data_to_file(output_filename, result):
    with open(output_filename, "w", encoding="utf-8") as file:
        file.writelines(result)
