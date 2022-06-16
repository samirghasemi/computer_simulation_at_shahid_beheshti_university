import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt

erdos = nx.erdos_renyi_graph(30, 0.3)
wats = nx.watts_strogatz_graph(30, 4, 0.3)
barabasi = nx.barabasi_albert_graph(30, 4)

sample_network = barabasi

life_time_pareto = []
life_time_expo = []
for i in range(nx.number_of_nodes(sample_network)):
    expo = np.random.exponential(2)
    expo_normal = np.around(expo, 3)
    life_time_expo.append(expo_normal)

for j in range(nx.number_of_nodes(sample_network)):
    pareto = np.around(np.random.pareto(1))
    pareto_norm = int(pareto)
    life_time_pareto.append(pareto_norm)

e_time_list = []
e_s_list = []
fi_list = []
average_degree_list = []
degree_a = 0
for i in range(nx.number_of_nodes(sample_network)):
    degree_a += sample_network.degree[i]
average_degree = degree_a / nx.number_of_nodes(sample_network)
average_degree_list.append(average_degree)
print(average_degree_list)


def deactive_lifetime():
    fi_time = 0
    degree = 0
    out = 0
    while True:
        fi_time = 0
        for n in range(nx.number_of_nodes(sample_network)):
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


active_life_time_pareto = []
active_life_time_expo = []
for i in range(nx.number_of_nodes(sample_network)):
    expo = np.random.exponential(2)
    expo_normal = np.around(expo, 3)
    active_life_time_expo.append(expo_normal)

for j in range(nx.number_of_nodes(sample_network)):
    pareto = np.around(np.random.pareto(1))
    pareto_norm = int(pareto)
    active_life_time_pareto.append(pareto_norm)

active_e_time_list = []
active_e_s_list = []
active_fi_list = []
average_degree_list = []


def active_lifetime():
    active_out = 0
    while True:
        active_fi_time = 0
        for n in range(nx.number_of_nodes(sample_network)):
            if active_life_time_pareto[n] > 0:
                active_out += (((1 + (active_life_time_pareto[n] - 1)) ** average_degree) - 1) / average_degree
                active_life_time_pareto[n] = active_life_time_pareto[n] - 1
            elif active_life_time_pareto[n] == 0:
                neighbors = list(sample_network.neighbors(n))
                for s in neighbors:
                    random_node = random.randint(0, nx.number_of_nodes(sample_network))
                    try:
                        sample_network.add_edge(s, random_node)
                    except:
                        pass
                # try:
                #     if sample_network.has_node(n):
                #         sample_network.remove_node()
                # except:
                #     pass

        try:
            active_e_s = (1 / np.sum(active_life_time_pareto)) * 10
            active_e_s_list.append(active_e_s)
        except:
            active_e_s_list.append(1)
        active_e_time_list.append(active_out)
        try:
            active_out_l = active_fi_time / active_out
        except:
            active_out_l = 0
        active_fi_list.append(active_out_l)
        if not np.any(active_life_time_pareto):
            break


deactive_lifetime()
# active_lifetime()
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
active_pareto_random = []

for j in range(len(active_fi_list)):
    d += np.random.pareto(1)
    pareto_random.append(d)

active_normal_random = []
s = 0
for j in range(len(active_fi_list)):
    s += np.random.normal(1)
    normal_random.append(s)

print(e_time_list)
print(average_degree_list)

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(list(range(len(e_time_list))), e_time_list)
plt.title("E[T]/K")
plt.ylabel('E[T]')
plt.xlabel('K')
ax.grid()
plt.savefig("4-1-deactive-barabasi.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(e_s_list, e_time_list)
plt.title("E[T]/E[S]")
plt.ylabel('E[T]')
plt.xlabel('E[S]')
ax.grid()
plt.savefig("4-2-deactive-barabasi.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.title("FI/E[S]")
plt.plot(e_s_list, fi_list)
plt.ylabel('Fi')
plt.xlabel('E[S]')
ax.grid()
plt.savefig("4-3-deactive-barabasi.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(pareto_random, fi_list)
plt.title('fi/Pareto distribution')
plt.ylabel('fi')
plt.xlabel('Pareto distribution')
ax.grid()
plt.savefig("4-4-deactive-barabasi.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.title('fi/Normal distribution')
plt.plot(normal_random, fi_list)
plt.ylabel('fi')
plt.xlabel('Normal distribution')
ax.grid()
plt.savefig("4-5-deactive-barabasi.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(list(range(len(e_time_list))), e_time_list)
plt.title("E[T]/K")
plt.ylabel('E[T]')
plt.xlabel('K')
ax.grid()
plt.savefig("4-1-active-erdos-reny.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(active_e_s_list, active_e_time_list)
plt.title("E[T]/E[S]")
plt.ylabel('E[T]')
plt.xlabel('E[S]')
ax.grid()
plt.savefig("4-2-active-erdos-reny.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.title("FI/E[S]")
plt.plot(active_e_s_list, active_fi_list)
plt.ylabel('Fi')
plt.xlabel('E[S]')
ax.grid()
plt.savefig("4-3-active-erdos-reny.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(active_pareto_random, active_fi_list)
plt.title('fi/Pareto distribution')
plt.ylabel('fi')
plt.xlabel('Pareto distribution')
ax.grid()
plt.savefig("4-4-active-erdos-reny.png")
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))
plt.title('fi/Normal distribution')
plt.plot(active_normal_random, active_fi_list)
plt.ylabel('fi')
plt.xlabel('Normal distribution')
ax.grid()
plt.savefig("4-5-active-erdos-reny.png")
plt.show()
