import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

import constants.colors as colors


def partition(arr, low, high, bar_plot, plot_placeholder, speed, fig):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

            bar_plot[i].set_height(arr[i])
            bar_plot[i].set_color(colors.ORANGE)
            bar_plot[j].set_height(arr[j])
            bar_plot[j].set_color(colors.ORANGE)

            plot_placeholder.pyplot(fig)
            time.sleep(speed)

            bar_plot[i].set_color(colors.BLUE)
            bar_plot[j].set_color(colors.BLUE)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    bar_plot[i + 1].set_height(arr[i + 1])
    bar_plot[i + 1].set_color(colors.ORANGE)
    bar_plot[high].set_height(arr[high])
    bar_plot[high].set_color(colors.ORANGE)

    plot_placeholder.pyplot(fig)
    time.sleep(speed)

    bar_plot[i + 1].set_color(colors.BLUE)
    bar_plot[high].set_color(colors.BLUE)

    return i + 1


def quick_sort_helper(arr, low, high, bar_plot, plot_placeholder, speed, fig):
    if low < high:
        pi = partition(arr, low, high, bar_plot, plot_placeholder, speed, fig)

        quick_sort_helper(arr, low, pi - 1, bar_plot, plot_placeholder, speed, fig)
        quick_sort_helper(arr, pi + 1, high, bar_plot, plot_placeholder, speed, fig)


def perform_and_display_quick_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    quick_sort_helper(lst, 0, len(lst) - 1, bar_plot, plot_placeholder, speed, fig)

    end_time = time.time()
    return lst, round(end_time - start_time, 2)
