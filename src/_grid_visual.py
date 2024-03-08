import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def visualize_grid_sequence(num_rows, num_cols, sequence):
    """
    Visualizes the order of cells in the sequence, using a color map.
    """

    # Create a grid initialized to NaN values
    grid = np.full((num_rows, num_cols), np.nan)

    # Fill the grid with indices reflecting the sequence order
    for order, (row, col) in enumerate(sequence):
        grid[row, col] = order

    # Normalize the sequence order to [0, 1] for color mapping
    normalized = grid / np.nanmax(grid)

    # Create a colormap (red to blue)
    colormap = mcolors.LinearSegmentedColormap.from_list("", ["red", "blue"])

    # Plot the grid
    plt.imshow(normalized, cmap=colormap, interpolation='nearest')

    # Optionally, add a colorbar to indicate the sequence order
    plt.colorbar(label='Sequence Order')

    plt.title('Grid Sequence Visualization')
    plt.xlabel('Column Index')
    plt.ylabel('Row Index')
    plt.show()
