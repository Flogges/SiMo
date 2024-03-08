""" Algorithm tests """

from src._cluster import Cluster
from src._cell import Cell
from src._grid import Grid
from src._cell_picker import CellPicker
from src._grid_visual import visualize_grid_sequence
# --------------------------------------------
def test_cell_picker_seq_random():
    """ visualize cell picker sequence """

    num_rows = 5
    num_cols = 6
    picker = CellPicker(num_rows, num_cols)
    seq = picker.seq_random(deterministic=False)



    uniq_vals = set(seq)
    uniq_cnt = len(uniq_vals)
    assert uniq_cnt == (num_rows * num_cols), "expect all values chosen exactly once"

    seq_orig = [(row, col) for row in range(num_rows) for col in range(num_cols)]

    # Count the differences between the original and shuffled sequences
    num_differ = sum(1 for orig, shuffled in zip(seq, seq_orig) if orig != shuffled)
    assert num_differ > 0 , "expect shuffled sequence to differ from original"

    # plot the sequence in colors reqpresenting sequence order
    visualize_grid_sequence(num_rows, num_cols, seq)
# --------------------------------------------
