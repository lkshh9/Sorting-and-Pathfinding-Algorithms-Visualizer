import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
import time
import constants.colors as colors


def perform_and_display_dfs(graph, start, end, speed):
    start_time = time.time()
    shortest_path = []
    visited_nodes = set()

    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph, seed=42)
    plt.title("DFS Shortest Path Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    def dfs_helper(current_node):
        nonlocal shortest_path

        visited_nodes.add(current_node)
        nx.draw(graph, pos, node_color=colors.BLUE, node_size=500, ax=ax)
        nx.draw_networkx_labels(
            graph,
            pos,
            labels={node: f"{node}" for node in graph.nodes},
            ax=ax,
        )
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=[current_node],
            node_color=colors.ORANGE,
            node_size=700,
            ax=ax,
        )

        plot_placeholder.pyplot(fig)
        time.sleep(speed)

        if current_node == end:
            shortest_path = nx.shortest_path(graph, start, end)
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                dfs_helper(neighbor)

    dfs_helper(start)

    if shortest_path:
        edge_colors = [
            colors.ORANGE
            if (u, v) in zip(shortest_path, shortest_path[1:])
            else colors.BLUE
            for u, v in graph.edges
        ]

        node_colors = [
            colors.ORANGE if node in shortest_path else colors.BLUE
            for node in graph.nodes
        ]

        nx.draw(
            graph,
            pos,
            node_color=node_colors,
            node_size=500,
            edge_color=edge_colors,
            width=2.0,
            ax=ax,
        )

        nx.draw_networkx_labels(
            graph,
            pos,
            labels={node: node for node in graph.nodes},
            ax=ax,
        )

        edge_labels = {
            (node1, node2): graph[node1][node2]["weight"]
            for node1, node2 in graph.edges()
        }

        nx.draw_networkx_edge_labels(
            graph,
            pos,
            edge_labels=edge_labels,
            ax=ax,
        )

        plot_placeholder.pyplot(fig)
    else:
        st.warning("No Path Found")

    end_time = time.time()
    return shortest_path, len(shortest_path) - 1, round(end_time - start_time, 2)
