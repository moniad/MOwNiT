import itertools

V = 4  # no of vertices
start_v = 0
MAX_WEIGHT = 1e99999


def permutate(vertices):
    for p in itertools.permutations(vertices):
        yield p


def get_graph():
    return [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]


def travelling_salesman_problem():
    vertices = []
    for i in range(0, V):
        if i != start_v:
            vertices.append(i)

    # print("vertices: ", vertices)
    min_path_weight = MAX_WEIGHT

    for cur_vertices in permutate(vertices):
        cur_path_weight = 0
        cur_v = start_v
        for v in cur_vertices:
            cur_path_weight += graph[cur_v][v]
            cur_v = v

        cur_path_weight += graph[cur_v][start_v]  # adding the last edge to create a cycle
        min_path_weight = min(min_path_weight, cur_path_weight)

    return min_path_weight


def main():
    global graph
    graph = get_graph()

    print("Min path length = ", travelling_salesman_problem())


if __name__ == "__main__":
    main()
