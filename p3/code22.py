import math
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

erdos = nx.erdos_renyi_graph(4, 0.3)
wats = nx.watts_strogatz_graph(4, 2, 0.3)
barabasi = nx.barabasi_albert_graph(4, 3)

sample_network3 = barabasi


def deactive_lifetime(network):
    average_degree, life_time_pareto, life_time_expo = init_calculate(network)

    fi_list = []
    e_time_list = []
    e_s_list = []
    out = 0
    while True:
        fi_time = 0
        for n in range(nx.number_of_nodes(network)):
            if life_time_pareto[n] > 1:
                out += (((1 + (life_time_pareto[n] - 1)) ** average_degree) - 1) / average_degree
                fi_time += life_time_pareto[n] - 1
            if life_time_pareto[n] > 0:
                life_time_pareto[n] = life_time_pareto[n] - 1
            # try:
            #     if life_time_pareto[n] == 0:
            #         sample_network.remove_node(n)
            # except:
            #     pass

        try:
            e_s = (1 / np.sum(life_time_pareto)) * 10
            e_s_list.append(e_s)
        except:
            e_s_list.append(1)
        e_time_list.append(out)
        try:
            out_l = fi_time / out
        except:
            out_l = 0
        fi_list.append(out_l)
        if not np.any(life_time_pareto):
            break

    normal_random, pareto_random = random_generate(fi_list)

    return e_time_list, e_s_list, fi_list, pareto_random, normal_random


def random_generate(fi_list):
    pareto_random = []
    d = 0
    for j in range(len(fi_list)):
        d += np.random.pareto(1)
        pareto_random.append(d)
    normal_random = []
    s = 0
    for j in range(len(fi_list)):
        s += np.random.normal(1)
        normal_random.append(s)
    return normal_random, pareto_random


def init_calculate(network):
    life_time_pareto = []
    life_time_expo = []
    for i in range(nx.number_of_nodes(network)):
        expo = np.random.exponential(2)
        expo_normal = np.around(expo, 3)
        life_time_expo.append(expo_normal)
        pareto = np.around(np.random.pareto(1))
        pareto_norm = int(pareto)
        life_time_pareto.append(pareto_norm)
    degree_a = 0
    for i in range(nx.number_of_nodes(network)):
        degree_a += network.degree[i]
    average_degree = degree_a / nx.number_of_nodes(network)
    return average_degree, life_time_pareto, life_time_expo


def active_lifetime(network):
    average_degree, life_time_pareto, life_time_expo = init_calculate(network)

    e_time_list = []
    e_s_list = []
    fi_list = []
    out = 0
    while True:
        active_fi_time = 0
        for n in range(nx.number_of_nodes(network)):
            if life_time_pareto[n] > 0:
                out += (((1 + (life_time_pareto[n] - 1)) ** average_degree) - 1) / average_degree
                life_time_pareto[n] = life_time_pareto[n] - 1
            elif life_time_pareto[n] == 0:
                neighbors = list(network.neighbors(n))
                for s in neighbors:
                    random_node = random.randint(0, nx.number_of_nodes(network))
                    try:
                        network.add_edge(s, random_node)
                    except:
                        pass
                # try:
                #     if sample_network.has_node(n):
                #         sample_network.remove_node()
                # except:
                #     pass

        try:
            active_e_s = (1 / np.sum(life_time_pareto)) * 10
            e_s_list.append(active_e_s)
        except:
            e_s_list.append(1)
        e_time_list.append(out)
        try:
            active_out_l = active_fi_time / out
        except:
            active_out_l = 0
        fi_list.append(active_out_l)
        if not np.any(life_time_pareto):
            break

    normal_random, pareto_random = random_generate(fi_list)

    return e_time_list, e_s_list, fi_list, pareto_random, normal_random


def plots(e_time_list, e_s_list, fi_list, pareto_random, normal_random, network, type):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(list(range(len(e_time_list))), e_time_list)
    plt.title("E[T]/K")
    plt.ylabel('E[T]')
    plt.xlabel('K')
    ax.grid()
    plt.savefig('phase2/' + network + '/4-1-' + type + '.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(e_s_list, e_time_list)
    plt.title("E[T]/E[S]")
    plt.ylabel('E[T]')
    plt.xlabel('E[S]')
    ax.grid()
    plt.savefig('phase2/' + network + '/4-2-' + type + '.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.title("FI/E[S]")
    plt.plot(e_s_list, fi_list)
    plt.ylabel('Fi')
    plt.xlabel('E[S]')
    ax.grid()
    plt.savefig('phase2/' + network + '/4-3-' + type + '.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(pareto_random, fi_list)
    plt.title('fi/Pareto distribution')
    plt.ylabel('fi')
    plt.xlabel('Pareto distribution')
    ax.grid()
    plt.savefig('phase2/' + network + '/4-4-' + type + '.png')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 6))
    plt.title('fi/Normal distribution')
    plt.plot(normal_random, fi_list)
    plt.ylabel('fi')
    plt.xlabel('Normal distribution')
    ax.grid()
    plt.savefig('phase2/' + network + '/4-5-' + type + '.png')
    plt.show()


deactive_erdos_e_time_list, deactive_erdos_e_s_list, deactive_erdos_fi_list, deactive_erdos_pareto_random, deactive_erdos_normal_random = \
    deactive_lifetime(erdos)
