import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st
import time
import constants.colors as colors


def perform_and_display_bfs(graph, start, end, speed):
    start_time = time.time()
    shortest_path = []
    dist = {node: float("inf") for node in graph.nodes}
    dist[start] = 0

    fig, ax = plt.subplots()
    pos = nx.spring_layout(graph, seed=42)
    plt.title("BFS Shortest Path Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    queue = [(start, 0)]

    visited_nodes = set()

    while queue:
        print(f"Queue => {queue}, Visited Nodes => {visited_nodes}")
        current_node, current_dist = queue.pop(0)
        print(f"Current Node => {current_node}, Current Distance => {current_dist}")

        if current_node in visited_nodes:
            continue

        visited_nodes.add(current_node)
        print(f"Node Visited => {visited_nodes}")

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

        print("Sleep Time Done")
        if current_node == end:
            shortest_path = nx.shortest_path(graph, start, end)
            break

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited_nodes:
                new_distance = (
                    dist[current_node] + graph[current_node][neighbor]["weight"]
                )
                print(
                    f"New Distance => {dist[current_node]} + {graph[current_node][neighbor]['weight']} = {new_distance}"
                )
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance
                    queue.append((neighbor, new_distance))

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
    return shortest_path, dist[end], round(end_time - start_time, 2)
