def plot_default():
    ...

def plot_table():
    ...

def plot_bar_graph():
    ...

def plot_line_graph():
    ...

def plot_scatter_plot():
    ...


def run():
    plotting_functions = {
        "Default": plot_default,
        "Table": plot_table,
        "Bar Graph": plot_bar_graph,
        "Line Graph": plot_line_graph,
        "Scatter Plot": plot_scatter_plot,
    }

    graph_types = st.sidebar.multiselect("Graph Type", plotting_functions.keys())

    for graph_type in graph_types:
        plotting_functions[graph_type]()  # call function here
