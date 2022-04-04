import networkx as nx
from random import seed
from random import random
import matplotlib.pyplot as plt


def node_impair(G, p):
    result = G.copy()
    for node in G.nodes:
        rand_value = random()
        if rand_value < p:
            result.remove_node(node)
    return result


def edge_impair(G, p):
    result = G.copy()
    for edge in G.edges:
        rand_value = random()
        if rand_value < p:
            result.remove_edge(edge[0], edge[1])
    return result


print("Welcome to our simulator \n" +
      "for more information about this simulator and the inputs and outputs please read the help.txt file.")
print("In first please set the simulator parameters")
print()

print("1) which graph? please enter code of the graph")
print("for erdos_renyi enter 1 \nfor barabasi_albert enter 2\nfor watts_strogatz enter 3 ")
while True:
    code = int(input())
    if code == 1 or code == 2 or code == 3:
        break
    else:
        print("please enter a valid value")

while True:
    if code == 1:
        num_of_nodes = int(input("please enter number of nodes : "))
        p = float(input("enter the probability of edge creation : "))
        G = nx.erdos_renyi_graph(n=num_of_nodes, p=p)

    elif code == 2:
        num_of_nodes = int(input("please enter number of nodes : "))
        m = int(input("enter number of edges: "))
        G = nx.barabasi_albert_graph(n=num_of_nodes, m=m)

    else:
        num_of_nodes = int(input("please enter number of nodes : "))
        k = int(input("enter k nearest neighbours value : "))
        p = float(input("enter the probability of edge creation : "))
        G = nx.watts_strogatz_graph(n=num_of_nodes, k=k, p=p)

    if nx.is_connected(G):
        break
    else:
        print("It is not a connected graph. please try again ")

probability_of_impair = float(input("please enter the probability of impair : "))
impair_type = int(input("enter the code of impair type. 0 for node and 1 for edges : "))
number_of_simulations = int(input("please enter number of simulations : "))
seed_value = int(input("please enter the seed for random numbers : "))
seed(seed_value)

# nx.draw(G)
# plt.show()

#for _ in range(20):

num_of_isolated_graphs = 0
num_of_non_connected_graphs = 0
num_of_strongly_non_connected_graphs = 0


for _ in range(number_of_simulations):
    G_copy = G.copy()
    if impair_type == 0:
        G_copy = node_impair(G_copy, probability_of_impair)
    elif impair_type == 1:
        G_copy = edge_impair(G_copy, probability_of_impair)

    if not nx.is_connected(G_copy):
        num_of_non_connected_graphs += 1
    if len(list(nx.isolates(G_copy))) > 0:
        num_of_isolated_graphs += 1
    if not nx.strongly_connected_components(G_copy):
        num_of_strongly_non_connected_graphs += 1
    #print(str(num_of_strongly_non_connected_graphs / number_of_simulations))
    #print(str(num_of_nonconnected_graphs / number_of_simulations) + "            " + str(
    #    num_of_isolated_graphs / number_of_simulations))
    #probability_of_impair += 0.05

print("probability of generation of a connected graph is : " + str(num_of_non_connected_graphs / number_of_simulations))
print("probability of generation of a strongly connected graph is : " + str(num_of_strongly_non_connected_graphs / number_of_simulations))
print("probability of generation of a graph that contain isolated node is : "
     + str(num_of_isolated_graphs / number_of_simulations))
