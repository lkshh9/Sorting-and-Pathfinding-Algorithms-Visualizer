import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import string

from algorithms.pathfinding_algorithms.astar import perform_and_display_astar
from algorithms.pathfinding_algorithms.bfs import perform_and_display_bfs
from algorithms.pathfinding_algorithms.dfs import perform_and_display_dfs
from algorithms.pathfinding_algorithms.dijkstra import perform_and_display_dijkstra

from graphs.input_graph import draw_input_graph, set_up_custom_graph, set_up_input_graph


def algorithm_to_run(start, end, graph, speed, algo_title):
    if algo_title == "Breadth First Search":
        return perform_and_display_bfs(
            start=start,
            end=end,
            graph=graph,
            speed=speed,
        )
    elif algo_title == "Depth First Search":
        return perform_and_display_dfs(
            start=start,
            end=end,
            graph=graph,
            speed=speed,
        )
    elif algo_title == "Dijkstra's Algorithm":
        return perform_and_display_dijkstra(
            start=start,
            end=end,
            graph=graph,
            speed=speed,
        )
    elif algo_title == "A* Algorithm":
        return perform_and_display_astar(
            start=start,
            end=end,
            graph=graph,
            speed=speed,
        )


def display_pathfinding_layout():
    st.title("Pathfinding Algorithms Visualizer")

    algorithms_to_run = st.sidebar.multiselect(
        "Choose Algorithms to run: ",
        [
            "Breadth First Search",
            "Depth First Search",
            "Dijkstra's Algorithm",
            "A* Algorithm",
        ],
    )

    if len(algorithms_to_run) > 0:
        isAutoGenElement = st.sidebar.checkbox("Auto Generate Nodes?", value=True)
        if isAutoGenElement:
            num_nodes = st.sidebar.slider("Select the number of nodes (1-25):", 1, 25)
            input_nodes = num_nodes
            node_labels, pos, edge_labels, fig, ax, graph = set_up_input_graph(
                input_nodes
            )
            node_labels_list = list(node_labels)
            nodes_value_raw = "-1"
        else:
            nodes_value_raw = st.sidebar.text_area(label="Enter Nodes, Edges, Weights")
            st.sidebar.text("Example: AB2,AC4,BD1")
            if len(nodes_value_raw) > 0:
                (
                    graph,
                    node_labels_list,
                    pos,
                    fig,
                    ax,
                    edge_labels,
                ) = set_up_custom_graph(nodes_value_raw)
            else:
                node_labels_list = []

        if len(node_labels_list) > 0:
            source_node = st.sidebar.selectbox("Start Node: ", node_labels_list)
            dest_node_labels_list = node_labels_list.copy()
            dest_node_labels_list.remove(source_node)
            destination_node = st.sidebar.selectbox(
                "Desitnation Node: ", dest_node_labels_list
            )

        speed = st.sidebar.slider("Speed (ms)", min_value=1, max_value=1000, step=1)
        speed = speed / 1000

        should_run = st.sidebar.button("Run Algorithm", type="primary")

        min_time_taken = 999
        fastest_algo_result = st.empty()
        if should_run:
            col1, col2 = st.columns(2)
            for i in range(len(algorithms_to_run)):
                if (i + 1) % 2 != 0:
                    with col1:
                        (
                            shortest_path,
                            distance,
                            time_taken,
                        ) = algorithm_to_run(
                            start=source_node,
                            end=destination_node,
                            graph=graph,
                            speed=speed,
                            algo_title=algorithms_to_run[i],
                        )
                        st.text(
                            f"Total Time Taken: {time_taken} seconds\nShortest Path : {' => '.join(shortest_path)}"
                        )
                        if time_taken < min_time_taken:
                            min_time_taken = time_taken
                            fastest_algo_result.success(
                                f"{algorithms_to_run[i]} was the fastest to sort all the elements in {time_taken} seconds"
                            )
                else:
                    with col2:
                        (
                            shortest_path,
                            distance,
                            time_taken,
                        ) = algorithm_to_run(
                            start=source_node,
                            end=destination_node,
                            graph=graph,
                            speed=speed,
                            algo_title=algorithms_to_run[i],
                        )
                        st.text(
                            f"Total Time Taken: {time_taken} seconds\nShortest Path : {' => '.join(shortest_path)}"
                        )
                        if time_taken < min_time_taken:
                            min_time_taken = time_taken
                            fastest_algo_result.success(
                                f"{algorithms_to_run[i]} was the fastest to sort all the elements in {time_taken} seconds"
                            )

        else:
            if len(nodes_value_raw) > 0:
                draw_input_graph(graph, pos, ax, edge_labels, fig)
