import networkx as nx
import matplotlib.pyplot as plt
import random


def nodes_connected(graph, u, v):
    return u in graph.neighbors(v)


def req1():
    num_of_nodes = int(input("please enter number of nodes : "))
    p = float(input("enter the probability of edge creation : "))
    num_of_simulation = int(input("please enter number of simulation : "))
    for i in range(num_of_simulation):
        graph = nx.erdos_renyi_graph(n=num_of_nodes, p=p)
        all_degrees = list(dict((nx.degree(graph))).values())
        unique_degree = list(set(all_degrees))
        unique_degree.sort()
        nodes_with_degree = []
        for i in unique_degree:
            nodes_with_degree.append(all_degrees.count(i))
        plt.plot(unique_degree, nodes_with_degree)
    plt.xlabel("Degrees")
    plt.ylabel("No. of nodes")
    plt.title("Degree distribution")
    plt.show()


def plot_probability_distribution(p_is_connected):
    plt.plot(p_is_connected)
    plt.ylabel("p")
    plt.xlabel("No. of edges")
    plt.title("p distribution")
    plt.show()


def req2():
    num_of_nodes = int(input("please enter number of nodes : "))
    num_of_edges = int(input("please enter number of edges : "))
    num_of_simulation = int(input("please enter number of simulation : "))
    # init probability graph
    graphs = []
    graphs_is_connected = []
    p_is_connected = []
    for i in range(0, num_of_simulation):
        graph = nx.Graph()
        graph.add_nodes_from(range(1, num_of_nodes + 1))
        graphs.append(graph)
        graphs_is_connected.append(False)
    # add edges and calculate probability
    for i in range(0, num_of_edges):
        p = 0
        for j, graph in enumerate(graphs):
            if graphs_is_connected[j]:
                p = p + 1
                continue;
            u = random.randint(1, num_of_nodes)
            v = random.randint(1, num_of_nodes)
            while u == v or nodes_connected(graph, u, v):
                u = random.randint(1, num_of_nodes)
                v = random.randint(1, num_of_nodes)

            graph.add_edge(u, v)
            if nx.is_connected(graph):
                p = p + 1
                graphs_is_connected[j] = True
        p_is_connected.append(p / num_of_simulation)
    plot_probability_distribution(p_is_connected)


def req3():
    num_of_nodes = int(input("please enter number of nodes : "))
    p = float(input("enter the probability of edge creation : "))

    graph = nx.erdos_renyi_graph(n=num_of_nodes, p=p)
    graph_init = graph.copy()
    fitness = []
    # nx.draw(graph, with_labels=True)
    # plt.show()
    for n in range(num_of_nodes):
        fitness.append(random.random())
    for i in range(10):
        edges = list(graph.edges)
        nonedges = list(nx.non_edges(graph))
        # random edge choice
        chosen_edge = random.choice(edges)
        list_of_neighbours = []

        for x in nonedges:
            if chosen_edge[0] == x[0]:
                list_of_neighbours.append((x[1], float(fitness[x[1]] * graph.degree[x[1]])))

        if len(list_of_neighbours) == 0:
            continue

        list_of_neighbours = sort_tuple(list_of_neighbours)
        chosen_node = list_of_neighbours[-1][0]
        # chosen_nonedge = random.choice([x for x in nonedges if chosen_edge[0] == x[0]])
        print(chosen_edge[0], chosen_edge[1])
        graph.remove_edge(chosen_edge[0], chosen_edge[1])
        # add new edge
        graph.add_edge(chosen_edge[0], chosen_node)
        print(chosen_edge[0], chosen_node)

    nx.draw(graph, with_labels=True)
    plt.show()


def sort_tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


if __name__ == '__main__':
    req = int(input("select your request!"
                    "\n1 - req1"
                    "\n2 - req2"
                    "\n3 - req3"))
    while True:
        if req == 1:
            req1()
            break
        elif req == 2:
            req2()
            break
        elif req == 3:
            req3()
            break
        else:
            print("please select again!")
