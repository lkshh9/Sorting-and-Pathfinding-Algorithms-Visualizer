import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

import constants.colors as colors


def counting_sort(arr, exp, bar_plot, plot_placeholder, speed, fig):
    n = len(arr)
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

        bar_plot[i].set_color(colors.ORANGE)
        bar_plot[i].set_height(output[count[index]])

        plot_placeholder.pyplot(fig)
        time.sleep(speed)
        bar_plot[i].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)

    for i in range(n):
        arr[i] = output[i]
        bar_plot[i].set_color(colors.ORANGE)
        bar_plot[i].set_height(arr[i])

        plot_placeholder.pyplot(fig)
        time.sleep(speed)
        bar_plot[i].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)


def radix_sort(arr, bar_plot, plot_placeholder, speed, fig):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp, bar_plot, plot_placeholder, speed, fig)
        exp *= 10


def perform_and_display_radix_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    radix_sort(lst, bar_plot, plot_placeholder, speed, fig)

    end_time = time.time()
    return lst, round(end_time - start_time, 2)
