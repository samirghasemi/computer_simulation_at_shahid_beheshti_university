# Implementation of Erdos-Renyi Model on a Social Network
'''
This graph is sometimes called the Erdős-Rényi graph but is different from G{n,p} or binomial_graph which is also sometimes called the Erdős-Rényi graph.
'''

# Import Required modules
import networkx as nx
import matplotlib.pyplot as plt
import random


# Distribution graph for Erdos_Renyi model
def distribution_graph(g):
    print(nx.degree(g))
    all_node_degree = list(dict((nx.degree(g))).values())

    unique_degree = list(set(all_node_degree))
    unique_degree.sort()
    nodes_with_degree = []
    for i in unique_degree:
        nodes_with_degree.append(all_node_degree.count(i))

    plt.plot(unique_degree, nodes_with_degree)
    plt.xlabel("Degrees")
    plt.ylabel("No. of nodes")
    plt.title("Degree distribution")
    plt.show()


def main():
    # Take N number of nodes from user
    print("Enter number of nodes")
    N = int(input())

    # Take P probability value for edges
    print("Enter value of probability of every node")
    P = float(input())

    # Create an empty graph object
    g = nx.Graph()

    # Adding nodes
    g.add_nodes_from(range(1, N + 1))

    # Add edges to the graph randomly.
    for i in g.nodes():

        for j in g.nodes():
            if (i < j):
                # Take random number R.
                R = random.random()

                # Check if R<P add the edge to the graph else ignore.
                if (R < P):
                    g.add_edge(i, j)
        pos = nx.circular_layout(g)

        # some properties
        print("node degree clustering")
        for v in nx.nodes(g):
            print(f"{v} {nx.degree(g, v)} {nx.clustering(g, v)}")

        print("================================")
        print("the adjacency list")
        for line in nx.generate_adjlist(g):
            print(line)
        print("================================")
        # Display the social network
        nx.draw(g, pos, with_labels=1)
        plt.show()

    # Display connection between nodes
    distribution_graph(g)

if __name__ == '__main__':
    main()
