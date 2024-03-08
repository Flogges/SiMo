""" Algorithm tests """

from src._cluster import Cluster
from src._cell import Cell
from src._grid import Grid
from src._cell_picker import CellPicker
from src._grid_visual import visualize_grid_sequence
# --------------------------------------------
def test_grid_create():
    """ test algorithm creation() """

    num_rows = 5
    num_cols = 6
    grid = Grid(num_rows, num_cols)
    picker = CellPicker(num_rows, num_cols)
    seq = picker.seq_random(deterministic=False)

    visualize_grid_sequence(num_rows, num_cols, seq)

    print(f"seq...{seq}")
