import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

import constants.colors as colors


def perform_and_display_insertion_sort(x, lst, title, speed):
    start_time = time.time()
    fig, ax = plt.subplots()
    bar_plot = ax.bar(x, lst, color=colors.BLUE)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_title(f"{title} Visualization")

    plot_placeholder = st.empty()
    plot_placeholder.pyplot(fig)

    n = len(lst)
    for i in range(1, n):
        key = lst[i]

        j = i - 1

        while j >= 0 and key < lst[j]:
            bar_plot[j].set_color(colors.ORANGE)
            bar_plot[j + 1].set_color(colors.ORANGE)
            plot_placeholder.pyplot(fig)

            time.sleep(speed)

            lst[j + 1] = lst[j]
            j = j - 1

            bar_plot[j].set_height(lst[j])
            bar_plot[j + 1].set_height(lst[j + 1])
            bar_plot[j].set_color(colors.BLUE)
            bar_plot[j + 1].set_color(colors.BLUE)
            plot_placeholder.pyplot(fig)

        bar_plot[i].set_height(lst[i])
        bar_plot[j + 1].set_height(lst[j + 1])
        bar_plot[i].set_color(colors.BLUE)
        bar_plot[j + 1].set_color(colors.BLUE)
        plot_placeholder.pyplot(fig)
        lst[j + 1] = key

    end_time = time.time()

    return lst, round(end_time - start_time, 2)
