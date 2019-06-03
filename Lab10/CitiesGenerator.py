from City import City
import random
import numpy as np


def generate_random(num_points):
    cities = []
    for _ in range(num_points):
        cities.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
    return cities


def generate_norm_dis(num_points, centre_y=0.0, centre_x=0.0, deviation_y=1.0, deviation_x=1.0):
    cities = []
    for _ in range(num_points):
        cities.append(City(
            x=int(np.random.normal(centre_x, deviation_x) * 200),
            y=int(np.random.normal(centre_y, deviation_y) * 200)))
    return cities


def generate_nine_groups(num_points):
    cities = []
    group_centers = [30, 100, 170]
    for i in range(num_points // 3):
        for j in range(3):
            cities.append(City(
                x=int(np.random.normal(group_centers[i % 3], 10.0)),
                y=int(np.random.normal(group_centers[j % 3], 10.0))))
    return cities
