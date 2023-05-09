# find the nearest location
def find_nearest(location, locations, visited):
    optimal_distance = float('inf')

    for index, loc in enumerate(locations):
        if index in visited:
            continue
        else:
            distance = (location[0] - loc[0]) ** 2 + (location[1] - loc[1]) ** 2 + (location[2] - loc[2]) ** 2
            if optimal_distance > distance:
                optimal_distance = distance
                i_nearest_location = index
                nearest_location = loc

    return i_nearest_location, nearest_location, optimal_distance


# use greedy to find optimal path
def greedy_alg(locations, num_locations):
    optimal_distance = float('inf')

    for i_start, start in enumerate(locations):
        distance = 0
        path = []
        path.append(i_start)
        i_next_location, next_location, dist = find_nearest(start, locations, path)
        distance += dist
        path.append(i_next_location)

        while num_locations > len(path):
            i_next_location, next_location, dist = find_nearest(next_location, locations, path)
            distance += dist
            path.append(i_next_location)

        if optimal_distance > distance:
            optimal_distance = distance
            optimal_path = path

    first = optimal_path.index(0)
    reorder = optimal_path[first:] + optimal_path[0:first]
    reorder.append(0)
    optimal_path = reorder

    return optimal_path, optimal_distance


def main():
    # read the input coordinates
    input_file_path = r'input.txt'
    locations = []
    input_f = open(input_file_path, 'r', encoding='utf-8')
    input_list = input_f.read().splitlines()
    input_f.close()
    num_locations = int(input_list.pop(0))
    for coordinate in input_list:
        coord_map = map(int, coordinate.split())
        coord_tuple = tuple(coord_map)
        locations.append(coord_tuple)

    # calculate the optimal path
    optimal_path, optimal_distance = greedy_alg(locations, num_locations)

    # write the answer into output file
    output_file_path = r'output.txt'
    output_f = open(output_file_path, 'w', encoding='utf-8')
    for location in optimal_path:
        output_f.write(str(locations[location][0]) + ' ')
        output_f.write(str(locations[location][1]) + ' ')
        output_f.write(str(locations[location][2]) + '\n')
    output_f.close()


if __name__ == '__main__':
    main()
