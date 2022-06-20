import math
import networkx as nx
import matplotlib.pyplot as plt




number_of_nodes = 50
p_graph = 0.2
deg = 10

# Erdos-Reny graph-------------------
erdos_network = nx.erdos_renyi_graph(number_of_nodes, p_graph)

# [e_list, eq3_list] = calculation_eq3(erdos_network)
# plot_reducibility(e_list, eq3_list, 'Erdos-Reny')

[e_list, eq6_list] = calculation_eq6(erdos_network)
plot_reliability(e_list, eq6_list, 'Erdos-Reny')
# -----------------------------------


watts_network = nx.watts_strogatz_graph(number_of_nodes, deg, p)
# [w_list, w_out_list, w_ki_list] = calculation_eq3(watts_network)
# plot_reducibility(w_list, w_ki_list, 'Watts-Strogatz')
# # plot_reliability(w_list, w_out_list, 'Watts-Strogatz')
#
barabasi_network = nx.barabasi_albert_graph(number_of_nodes, deg)
# [b_list, b_out_list, b_ki_list] = calculation_eq3(barabasi_network)
# plot_reducibility(b_list, b_ki_list, 'Barabasi-Albert')
# # plot_reliability(b_list, b_out_list, 'Barabasi-Albert')
