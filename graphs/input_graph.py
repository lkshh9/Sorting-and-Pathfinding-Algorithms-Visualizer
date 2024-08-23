import string, random
import networkx as nx
import matplotlib.pyplot as plt
import constants.colors as colors
import streamlit as st


@st.cache_resource
def set_up_input_graph(num_nodes):
    graph = nx.Graph()
    node_labels = string.ascii_uppercase[:num_nodes]
    graph.add_nodes_from(node_labels)

    for node1 in node_labels:
        for node2 in node_labels:
            if node1 != node2 and not graph.has_edge(node1, node2):
                weight = random.randint(1, 10)
                graph.add_edge(node1, node2, weight=weight)

    pos = nx.spring_layout(graph)

    edge_labels = {
        (node1, node2): graph[node1][node2]["weight"] for node1, node2 in graph.edges()
    }

    fig_size = min(10 + num_nodes, 20)
    fig, ax = plt.subplots(figsize=(fig_size, fig_size))
    return node_labels, pos, edge_labels, fig, ax, graph


@st.cache_resource
def set_up_custom_graph(nodes_value_raw):
    graph = nx.Graph()
    nodes_value_list = nodes_value_raw.split(",")
    unique_nodes = set()
    for i in range(len(nodes_value_list)):
        nodes_value_list[i] = nodes_value_list[i].lstrip().rstrip()
        unique_nodes.add(nodes_value_list[i][0])
        unique_nodes.add(nodes_value_list[i][1])
        graph.add_edge(
            nodes_value_list[i][0],
            nodes_value_list[i][1],
            weight=int(nodes_value_list[i][2:]),
        )
    node_labels_list = sorted(unique_nodes)
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    edge_labels = {
        (node1, node2): graph[node1][node2]["weight"] for node1, node2 in graph.edges()
    }
    return graph, node_labels_list, pos, fig, ax, edge_labels


def draw_input_graph(graph, pos, ax, edge_labels, fig):
    nx.draw_networkx_nodes(graph, pos, ax=ax, node_color=colors.BLUE, node_size=500)
    nx.draw_networkx_edges(graph, pos, ax=ax, edge_color=colors.BLUE, width=2)
    nx.draw_networkx_labels(
        graph,
        pos,
        labels={node: node for node in graph.nodes()},
        ax=ax,
        font_size=14,
        font_color="white",
    )

    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels=edge_labels, ax=ax, font_size=14, font_color="black"
    )

    ax.set_title("Input Graph")
    ax.set_xticks([])
    ax.set_yticks([])
    st.pyplot(fig)
