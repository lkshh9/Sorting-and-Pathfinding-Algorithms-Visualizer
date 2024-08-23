import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

import constants.colors as colors


def perform_and_display_selection_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            bar_plot[j].set_color(colors.ORANGE)
            bar_plot[min_idx].set_color(colors.ORANGE)
            plot_placeholder.pyplot(fig)

            time.sleep(speed)

            if lst[j] < lst[min_idx]:
                min_idx = j

            bar_plot[j].set_height(lst[j])
            bar_plot[min_idx].set_height(lst[min_idx])
            bar_plot[j].set_color(colors.BLUE)
            bar_plot[min_idx].set_color(colors.BLUE)
            plot_placeholder.pyplot(fig)
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

        bar_plot[i].set_height(lst[i])
        bar_plot[min_idx].set_height(lst[min_idx])
        bar_plot[i].set_color(colors.BLUE)
        bar_plot[min_idx].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)

    end_time = time.time()
    return lst, round(end_time - start_time, 2)
