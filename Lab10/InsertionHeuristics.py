import matplotlib.pyplot as plt
import networkx as nx
from numpy import inf

from CitiesGenerator import *


def get_current_cycle_len(cities):
    cycle_len = 0

    for i in range(1, len(cities)):
        cycle_len += cities[i - 1].distance(cities[i])

    last_city = cities[len(cities) - 1]
    cycle_len += last_city.distance(cities[0])  # start_city_ind = 0

    return cycle_len

# it's not a simple random pick
def find_farthest_city_from_cycle(cur_cities_in_cycle, cities_to_add_to_cycle):
    max_distance = -1
    max_dist_city = cities_to_add_to_cycle[0]
    for city in cities_to_add_to_cycle:
        cur_distance = 0
        for city_in_cycle in cur_cities_in_cycle:
            cur_distance += city.distance(city_in_cycle)
        if cur_distance > max_distance:
            max_distance = cur_distance
            max_dist_city = city

    return max_dist_city


def randomly_find_city_to_add_to_cycle(cities):
    # randomly picking the city
    if len(cities) == 0:
        print("No cities to add to cycle left!")
        return None
    ind = random.randint(0, len(cities) - 1)
    return cities[ind]


def find_new_city_index(cur_cities_in_cycle, new_city):  # index is an index in cur_cities_in_cycle table
    cycle_len = get_current_cycle_len(cur_cities_in_cycle)
    min_cycle_len = inf
    # print("min cycle len: ", min_cycle_len, " vs cycle_len: ", cycle_len)
    index = -1
    len_of_cycle = len(cur_cities_in_cycle)

    # farthest insertion
    for i in range(1, len_of_cycle):
        new_cycle_len = cycle_len - cur_cities_in_cycle[i-1].distance(cur_cities_in_cycle[i % len_of_cycle]) + \
                        cur_cities_in_cycle[i-1].distance(new_city) + new_city.distance(cur_cities_in_cycle[i % len_of_cycle])

        if new_cycle_len < min_cycle_len:
            index = i
            min_cycle_len = new_cycle_len

    # print("cur cities in cycle: ", cur_cities_in_cycle)
    if index == -1 and cycle_len > 1:
        print("Index = -1, couldn't find any optimal place for our city! :(")
    # else:
    #     print("index = ", index)
    return index


def travelling_salesman_problem(cities):
    cities_to_add_to_cycle = [i for i in cities]
    # print("cities ... ", cities_to_add_to_cycle)
    cur_cities_in_cycle = []

    global start_city
    start_city = cities_to_add_to_cycle[0]
    cities_to_add_to_cycle.remove(start_city)

    cur_cities_in_cycle.append(start_city)

    # print("cities ... ", cities_to_add_to_cycle)

    # print("cur cycle len: ", get_current_cycle_len(cur_cities_in_cycle))

    for _ in range(0, len(cities_to_add_to_cycle)):
        city_to_add = randomly_find_city_to_add_to_cycle(cities_to_add_to_cycle)
        # city_to_add = find_farthest_city_from_cycle(cur_cities_in_cycle, cities_to_add_to_cycle)
        new_city_ind = find_new_city_index(cur_cities_in_cycle, city_to_add)
        cur_cities_in_cycle.insert(new_city_ind, city_to_add)
        cities_to_add_to_cycle.remove(city_to_add)
        # print("city_to_add, w zasadzie to_remove: ", city_to_add, " vs cur_cities_in_cycle: ", cur_cities_in_cycle, " vs cities_to_add: ", cities_to_add_to_cycle)

    plot(cur_cities_in_cycle)
    return get_current_cycle_len(cur_cities_in_cycle)


def plot(pop):  # population
    G = nx.Graph()
    G.add_edges_from([(pop[i], pop[i + 1]) for i in range(len(pop) - 1)])
    pos = {pop[i]: (pop[i].x, pop[i].y) for i in range(len(pop))}

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='k', node_size=10)
    nx.draw_networkx_edges(G, pos, G.edges(), edge_color='k', width=0.6)

    plt.gca().set_title('Resulting path')

    plt.show()


def main():
    cityListRandom = generate_random(27)
    # print("City List random: ", cityListRandom)
    cityListNormalDistribution = generate_norm_dis(27)
    cityListNineGroups = generate_nine_groups(27)

    print("Random City List. Min path length = ", travelling_salesman_problem(cityListRandom))
    print("Normal City Distribution. Min path length = ", travelling_salesman_problem(cityListNormalDistribution))
    print("Nine City Groups. Min path length = ", travelling_salesman_problem(cityListNineGroups))


if __name__ == "__main__":
    main()
