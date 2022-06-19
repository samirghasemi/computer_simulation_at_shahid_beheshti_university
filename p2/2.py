import math
import networkx as nx
import numpy as np
import random
import scipy as sp
import matplotlib.pyplot as plt

erdos_network = nx.erdos_renyi_graph(20,0.3)
watts_network = nx.watts_strogatz_graph(20,2,0.3)
barabasi_network = nx.barabasi_albert_graph(20,2)

p = 0
p_ki_list = []
p_list = []
out_g = 0
out_g_list = []

while p < 1:
    p_ki = 0
    for i in nx.degree(erdos_network):
        p_ki += p ** i[1]
    prob = -(1-p)*p_ki
    prob_e = math.e ** prob
    p_list.append(p)
    p_ki_list.append(prob_e)
    p += 0.01

    for j in range(nx.number_of_nodes(erdos_network)):
        cut = 0
        for n in list(nx.all_node_cuts(erdos_network)):
            if len(n) == j:
                cut += 1
        out_g += cut * (p ** j) * (1-p)**(nx.number_of_nodes(erdos_network)-j)

    out_g_list.append(1-out_g)



w = 0
w_ki_list = []
w_list = []
out_w = 0
out_w_list = []
while w < 1:
    w_ki = 0
    for i in nx.degree(watts_network):
        w_ki += w ** i[1]
    prob = -(1-w)*w_ki
    prob_e = math.e ** prob
    w_list.append(w)
    w_ki_list.append(prob_e)
    w += 0.01

    for j in range(nx.number_of_nodes(watts_network)):
        cut = 0
        for n in list(nx.all_node_cuts(watts_network)):
            if len(n) == j:
                cut += 1
        out_w += cut * (w ** j) * (1-w)**(nx.number_of_nodes(watts_network)-j)
    out_w_list.append(1-out_w)

b = 0
b_ki_list = []
b_list = []
out_b = 0
out_b_list = []
while b < 1:
    b_ki = 0
    for i in nx.degree(barabasi_network):
        b_ki += b ** i[1]
    prob = -(1-b)*b_ki
    prob_e = math.e ** prob
    b_list.append(b)
    b_ki_list.append(prob_e)
    b += 0.01

    for j in range(nx.number_of_nodes(barabasi_network)):
        cut = 0
        for n in list(nx.all_node_cuts(barabasi_network)):
            if len(n) == j:
                cut += 1
        out_b += cut * (b ** j) * (1-b)**(nx.number_of_nodes(barabasi_network)-j)
    out_b_list.append(1-out_b)


fig, ax = plt.subplots(figsize=(8, 6))
plt.plot(p_list,out_g_list)
plt.title('Erdos-reny network(reliability)')
plt.ylabel('تاب آوری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-6-erdos-reny.png')
plt.show()

plt.plot(p_list,p_ki_list)
plt.title('Erdos-reny network(connected)')
plt.ylabel('احتمال همبندی گراف')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-3-erdos-reny.png')
plt.show()


plt.title('Watts-strogatz network(reliability)')
plt.plot(w_list,out_w_list)
plt.ylabel('تاب آوری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-6-Watts-strogatz.png')
plt.show()

plt.plot(w_list,w_ki_list)
plt.title('Watts-strogatz network(connected)')
plt.ylabel('احتمال همبندی گراف')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-3-Watts-strogatz.png')
plt.show()

plt.title('Barabasi-Albert network(reliability)')
plt.plot(b_list,out_b_list)
plt.ylabel('تاب آوری')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-6-Barabasi-Albert.png')
plt.show()

plt.plot(b_list,b_ki_list)
plt.title('Barabasi-Albert network(connected)')
plt.ylabel('احتمال همبندی گراف')
plt.xlabel('احتمال(p)')
ax.grid()
plt.savefig('2-3-Barabasi-Albert.png')
plt.show()

