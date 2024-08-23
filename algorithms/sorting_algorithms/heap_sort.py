import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import constants.colors as colors


def heapify(arr, n, i, bar_plot, plot_placeholder, speed, fig):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        bar_plot[i].set_color(colors.ORANGE)
        bar_plot[largest].set_color(colors.ORANGE)
        bar_plot[i].set_height(arr[i])
        bar_plot[largest].set_height(arr[largest])
        plot_placeholder.pyplot(fig)
        time.sleep(speed)
        bar_plot[i].set_color(colors.BLUE)
        bar_plot[largest].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)

        heapify(arr, n, largest, bar_plot, plot_placeholder, speed, fig)


def heap_sort(lst, bar_plot, plot_placeholder, speed, fig):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i, bar_plot, plot_placeholder, speed, fig)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]

        bar_plot[0].set_color(colors.ORANGE)
        bar_plot[i].set_color(colors.ORANGE)
        bar_plot[0].set_height(lst[0])
        bar_plot[i].set_height(lst[i])
        plot_placeholder.pyplot(fig)
        time.sleep(speed)
        bar_plot[0].set_color(colors.BLUE)
        bar_plot[i].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)
        heapify(lst, i, 0, bar_plot, plot_placeholder, speed, fig)


def perform_and_display_heap_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    heap_sort(lst, bar_plot, plot_placeholder, speed, fig)

    end_time = time.time()
    return lst, round(end_time - start_time, 2)
