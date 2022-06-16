import networkx as nx
import numpy as np
import random
import scipy as sp
import matplotlib.pyplot as plt

erdos_network = nx.erdos_renyi_graph(20,0.3)
watts_network = nx.watts_strogatz_graph(20,2,0.3)
barabasi_network = nx.barabasi_albert_graph(20,2)

p = 0
p_list = []
random_num = np.random

is_reduced = 0
is_reduced_list = []
while p < 1:
    for i in range(0,999):
        for j in nx.edges(erdos_network):
            if random.random() < p:
                erdos_network.remove_edge(j[0],j[1])
        matrix = nx.adjacency_matrix(erdos_network).todense()
        if np.allclose(matrix, np.tril(matrix)) or np.allclose(matrix, np.triu(matrix)) or np.allclose(matrix, np.diag(np.diag(matrix))):
            is_reduced += 1
    is_reduced = 1 - (is_reduced/1000)
    is_reduced_list.append(is_reduced)
    p_list.append(p)
    p += 0.01


w = 0
w_list = []
is_reduced_w = 0
is_reduced_list_w = []
while w < 1:
    for i in range(0,999):
        for j in nx.edges(erdos_network):
            if random.random() < w:
                watts_network.remove_edge(j[0],j[1])
        matrix = nx.adjacency_matrix(watts_network).todense()
        if np.allclose(matrix, np.tril(matrix)) or np.allclose(matrix, np.triu(matrix)) or np.allclose(matrix, np.diag(np.diag(matrix))):
            is_reduced_w += 1
    is_reduced_w = 1 - (is_reduced_w/1000)
    is_reduced_list_w.append(is_reduced_w)
    w_list.append(w)
    w += 0.01

b = 0
b_list = []
is_reduced_b = 0
is_reduced_list_b = []
while b < 1:
    for i in range(0,999):
        for j in nx.edges(barabasi_network):
            if random.random() < b:
                barabasi_network.remove_edge(j[0],j[1])
        matrix = nx.adjacency_matrix(barabasi_network).todense()
        if np.allclose(matrix, np.tril(matrix)) or np.allclose(matrix, np.triu(matrix)) or np.allclose(matrix, np.diag(np.diag(matrix))):
            is_reduced_b += 1
    is_reduced_b = 1 - (is_reduced_b/1000)
    is_reduced_list_b.append(is_reduced_b)
    b_list.append(b)
    b += 0.01

fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(p_list,is_reduced_list)
plt.title('1-erdos-reny')
plt.ylabel('احتمال کاهش ناپذیری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('1-erdos-reny.png')
plt.show()

plt.plot(w_list,is_reduced_list_w)
plt.title('1-watts-strogatz')
plt.ylabel('احتمال کاهش ناپذیری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('1-watts-strogatz.png')
plt.show()

plt.plot(b_list,is_reduced_list_b)
plt.title('1-barabasi-albert')
plt.ylabel('احتمال کاهش ناپذیری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('1-barabasi-albert.png')
plt.show()




