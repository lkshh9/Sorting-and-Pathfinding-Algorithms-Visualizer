import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from algorithms.sorting_algorithms.bubble_sort import perform_and_display_bubble_sort
from algorithms.sorting_algorithms.selection_sort import (
    perform_and_display_selection_sort,
)
from algorithms.sorting_algorithms.insertion_sort import (
    perform_and_display_insertion_sort,
)
from algorithms.sorting_algorithms.merge_sort import perform_and_display_merge_sort
from algorithms.sorting_algorithms.quick_sort import perform_and_display_quick_sort
from algorithms.sorting_algorithms.radix_sort import perform_and_display_radix_sort
from algorithms.sorting_algorithms.heap_sort import perform_and_display_heap_sort

st.set_page_config(page_title="Matplotlib Plots", layout="centered")


def algorithm_to_run(x, lst, algo_title, time_interval_sec):
    if algo_title == "Bubble Sort":
        return perform_and_display_bubble_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Selection Sort":
        return perform_and_display_selection_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Insertion Sort":
        return perform_and_display_insertion_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Merge Sort":
        return perform_and_display_merge_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Quick Sort":
        return perform_and_display_quick_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Radix Sort":
        return perform_and_display_radix_sort(x, lst, algo_title, time_interval_sec)
    elif algo_title == "Heap Sort":
        return perform_and_display_heap_sort(x, lst, algo_title, time_interval_sec)


def display_sorting_algorithm_layout():
    heading = st.markdown(
        """
        <h1 style='text-align: center; color: black;'>Sorting Algorithms Visualizer</h1>
    """,
        unsafe_allow_html=True,
    )

    input_elements = st.sidebar.empty()
    sorted_elements = st.sidebar.empty()

    algorithms_to_run = st.sidebar.multiselect(
        "Choose Algorithms to run: ",
        [
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Radix Sort",
            "Heap Sort",
        ],
    )

    if len(algorithms_to_run) > 0:
        isAutoGenElement = st.sidebar.checkbox("Auto Generate Elements?", value=True)

        if isAutoGenElement:
            x = np.linspace(0, 10, 100)
            amount = st.sidebar.slider("Amount of Elements: ", 5, 30, step=1)
            lst = np.random.randint(0, 100, amount)
        else:
            input_values_raw_string = st.sidebar.text_input("Enter Elements to sort")
            st.sidebar.text("Sample input: [3,4,2,1]")

            if len(input_values_raw_string) > 0:
                input_values = [int(val) for val in input_values_raw_string.split(",")]
            else:
                input_values = [0]

            lst = input_values.copy()

        sorted_list = []
        x = np.arange(0, len(lst), 1)
        m = st.markdown(
            """
        <style>

        div.stTitle{
            margin: auto;
            display: block;
            position:relative;
            top:3px;
        }

        div.stButton > button:first-child {
            background-color: #FF4B4B;
            color: white;
            height: 3em;
            width: 12em;
            border-radius:10px;
            margin: auto;
            display: block;
        }

        div.stButton > button:hover {
            background-color: #FF4B4B;
            border:2px solid #000000;
        }

        div.stButton > button:active {
            position:relative;
            top:3px;
        }

        div.stText

        </style>""",
            unsafe_allow_html=True,
        )

        time_interval = st.sidebar.slider(
            "Speed (ms)", min_value=1, max_value=1000, step=1
        )
        time_interval_sec = time_interval / 1000
        st.sidebar.text(time_interval_sec)
        should_run = st.sidebar.button("Run", type="primary")

        st.sidebar.subheader("Parameters")
        st.sidebar.write(f"Input Elements:")
        st.sidebar.text(lst)

        st.sidebar.text("Sorted Elements:")
        sorted_elements = st.sidebar.empty()

        min_time_taken = 999
        fastest_algo_result = st.empty()
        col1, col2 = st.columns(2)
        if should_run:
            for i in range(len(algorithms_to_run)):
                if (i + 1) % 2 != 0:
                    with col1:
                        result, time_taken = algorithm_to_run(
                            x.copy(),
                            lst.copy(),
                            algorithms_to_run[i],
                            time_interval_sec,
                        )
                        sorted_elements.text(result)
                        st.text(f"Total Time Taken: {time_taken} seconds")
                        if time_taken < min_time_taken:
                            min_time_taken = time_taken
                            fastest_algo_result.success(
                                f"{algorithms_to_run[i]} was the fastest to sort all the elements in {time_taken} seconds"
                            )
                else:
                    with col2:
                        result, time_taken = algorithm_to_run(
                            x.copy(),
                            lst.copy(),
                            algorithms_to_run[i],
                            time_interval_sec,
                        )
                        sorted_elements.text(result)
                        st.text(f"Total Time Taken: {time_taken} seconds")
                        if time_taken < min_time_taken:
                            min_time_taken = time_taken
                            fastest_algo_result.success(
                                f"{algorithms_to_run[i]} was the fastest to sort all the elements in {time_taken} seconds"
                            )

        plt.show()
