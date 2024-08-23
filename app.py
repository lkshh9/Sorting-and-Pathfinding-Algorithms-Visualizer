import streamlit as st
from streamlit_option_menu import option_menu

from layout.sorting_algorithms_layout import display_sorting_algorithm_layout
from layout.pathfinding_algorithms_layout import display_pathfinding_layout


def main():
    chooser = option_menu(
        menu_title=None,
        options=["Sorting Algorithms", "Pathfinding Algorithms"],
        icons=["bar-chart-fill", "diagram-3-fill"],
        default_index=0,
        orientation="horizontal",
    )

    if chooser == "Sorting Algorithms":
        display_sorting_algorithm_layout()
    elif chooser == "Pathfinding Algorithms":
        display_pathfinding_layout()


if __name__ == "__main__":
    main()
