import math
import networkx as nx
import matplotlib.pyplot as plt


def calculation(network):
    print("calculation")
    p = 0
    p_ki_list = []
    p_list = []
    out_g = 0
    out_g_list = []

    while p < 1:
        print(p)
        p_ki = 0

        for i in nx.degree(network):
            p_ki += p ** i[1]
        prob = -(1 - p) * p_ki
        prob_e = math.e ** prob
        p_list.append(p)
        p_ki_list.append(prob_e)
        p += 0.01

        for j in range(nx.number_of_nodes(network)):
            cut = 0
            for n in list(nx.all_node_cuts(network)):
                if len(n) == j:
                    cut += 1
            out_g += cut * (p ** j) * ((1 - p) ** (nx.number_of_nodes(network) - j))

        out_g_list.append(1 - out_g)
        # while_end

    return [p_list, out_g_list, p_ki_list]


def plot_reliability(my_list, out_list, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(my_list, out_list)
    plt.title(title + ' network(reliability)')
    plt.ylabel('reliability')
    plt.xlabel('probability')
    ax.grid()
    plt.savefig('phase1-p2/2-6-' + title + '.png')
    plt.show()


def plot_correlation(my_list, out_list, title):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(my_list, out_list)
    plt.title(title + ' network(correlation)')
    plt.ylabel('correlation')
    plt.xlabel('probability')
    ax.grid()
    plt.savefig('phase1-p2/2-3-' + title + '.png')
    plt.show()


erdos_network = nx.erdos_renyi_graph(30, 0.5)
watts_network = nx.watts_strogatz_graph(30, 3, 0.5)
barabasi_network = nx.barabasi_albert_graph(30, 3)

[e_list, e_out_list, e_ki_list] = calculation(erdos_network)
plot_reliability(e_list, e_out_list, 'Erdos-Reny')
plot_correlation(e_list, e_ki_list, 'Erdos-Reny')

[w_list, w_out_list, w_ki_list] = calculation(watts_network)
plot_reliability(w_list, w_out_list, 'Watts-Strogatz')
plot_correlation(w_list, w_ki_list, 'Watts-Strogatz')

[b_list, b_out_list, b_ki_list] = calculation(barabasi_network)
plot_reliability(b_list, b_out_list, 'Barabasi-Albert')
plot_correlation(b_list, b_ki_list, 'Barabasi-Albert')
