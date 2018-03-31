import random


import thread
from functools import reduce
from earth_distance import distance



def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    road_map = [tuple(line.strip('\n').split('\t')) for line in open(file_name, 'r')]

    road_map = [tuple(float(city[i]) if i > 1 else city[i] for i in range(len(city)))
                                                                        for city in road_map]

    return road_map

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    cities_lst = [city[1] + " - (" + str(city[2]) + "," + str(city[3]) + ") "
                                                                    for city in road_map]
    print(cities_lst)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """

    if len(road_map) > 2:
        lattiudes = [city[2] for city in road_map]
        longitudes = [city[3] for city in road_map]
        lattiudes2 = [lattiudes[(i + 1) % len(lattiudes)] for i in range(len(lattiudes))]
        longitudes2 = [longitudes[(i + 1) % len(longitudes)]  for i in range(len(longitudes))]
        intercity_dis = list(map(distance, lattiudes, longitudes, lattiudes2, longitudes2))
    else:
        lattiudes = [road_map[0][2]]
        longitudes = [road_map[0][3]]
        lattiudes2 = [road_map[1][2]]
        longitudes2 = [road_map[1][3]]
        intercity_dis = list(map(distance, lattiudes, longitudes, lattiudes2, longitudes2))

    return reduce(lambda x, y: x+y, intercity_dis)



def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at
    location `index+1` (or at `0`, if `index` refers to the last element
    in the list), swap their positions in the `road_map`, compute the
    new total distance, and return the tuple

        (new_road_map, new_total_distance)
    """

    adj_roadmap = road_map[:]
    adj_roadmap[index], adj_roadmap[index+1] = adj_roadmap[index+1], adj_roadmap[index]

    total_distance = compute_total_distance(adj_roadmap)

    return (adj_roadmap, total_distance)


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    adj_roadmap = road_map[:]
    adj_roadmap[index2], adj_roadmap[index1] = adj_roadmap[index1], adj_roadmap[index2]

    total_distance = compute_total_distance(adj_roadmap)

    return (adj_roadmap, total_distance)


def start_swap_cities_thread(road_map, distance):

    #print('thread 1')

    #for i in range(5000):


    index1 = int(len(road_map) * random.random())
    index2 = int(len(road_map) * random.random())

    optimal = (road_map[:], distance)

    if swap_cities(road_map, index1, index2)[1] < distance:
        optimal = swap_cities(road_map, index1, index2)
        road_map = optimal[0]
        distance = optimal[1]

    return optimal


def start_swap_adjacent_thread(road_map, distance):
    #print('thread 2')
    #for i in range(5000):
    index = int((len(road_map) -1) * random.random())


    optimal = (road_map[:], distance)

    if swap_adjacent_cities(road_map, index)[1] < distance:
        optimal = swap_adjacent_cities(road_map, index)
        road_map = optimal[0]
        distance = optimal[1]

    return optimal


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`,
    try `10000` swaps, and each time keep the best cycle found so far.
    After `10000` swaps, return the best cycle found so far.
    """

    new_road_map = road_map[:]
    cycle_distance = compute_total_distance(road_map)

    for i in range(10000):
        test = int(100 * random.random())
        if test < 50:
            optimal = start_swap_cities_thread(new_road_map, cycle_distance)
            new_road_map = optimal[0]
            cycle_distance = optimal[1]

        else:
            optimal = start_swap_adjacent_thread(new_road_map, cycle_distance)
            new_road_map = optimal[0]
            cycle_distance = optimal[1]

    return  optimal
    #thread.start_new_thread(start_swap_adjacent_thread, (road_map, optimal))
    #thread.start_new_thread(start_swap_cities_thread, (road_map, optimal))



def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """



    road_map = read_cities('city-data.txt')
    print(compute_total_distance(road_map))
    print_cities(road_map)
    optimal = find_best_cycle(road_map)
    print(optimal[1])
    pass

if __name__ == "__main__":

    main()
