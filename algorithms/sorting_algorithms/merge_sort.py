import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

import constants.colors as colors


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort_helper(arr, l, r, bar_plot, plot_placeholder, speed, fig):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_helper(arr, l, m, bar_plot, plot_placeholder, speed, fig)
        merge_sort_helper(arr, m + 1, r, bar_plot, plot_placeholder, speed, fig)

        merge(arr, l, m, r)

        for i in range(l, r + 1):
            bar_plot[i].set_height(arr[i])
            bar_plot[i].set_color(colors.ORANGE)

        plot_placeholder.pyplot(fig)
        time.sleep(speed)
        bar_plot[i].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)


def perform_and_display_merge_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    merge_sort_helper(lst, 0, len(lst) - 1, bar_plot, plot_placeholder, speed, fig)

    end_time = time.time()
    return lst, round(end_time - start_time, 2)
