import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from typing import List, Tuple

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

# -------------------------------------
def plot_grid_with_adjacent(num_rows, num_cols, row_idx, col_idx, adjacent_cells : List[Tuple[int, int]]):

    """
    Visualizes the grid of size (num_rows x num_cols) with cell at (row_idx, col_idx) and adjacent_cells
    using a color map.
    """

    grid = np.full((num_rows, num_cols, 3), 255)  # Start with an all-white grid

    # Color the original cell blue
    grid[row_idx, col_idx] = [0, 0, 255]

    # Color the adjacent cells yellow
    for r, c in adjacent_cells:
        grid[r, c] = [255, 255, 0]

    # Display the grid
    plt.imshow(grid.astype('uint8'), aspect='equal')

    # Add grid lines
    plt.grid(which='major', axis='both', linestyle='-', color='black', linewidth=2)
    plt.xticks(np.arange(-0.5, num_cols, 1))
    plt.yticks(np.arange(-0.5, num_rows, 1))

    # Hide tick labels
    plt.tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)

    plt.show()
