import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add Page Title
ui.page_opts(title="PyShiny Plot with Evan",fillable=True)

# Create sidebar with a slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 5, 50, 25)


@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_points: int = 425
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
