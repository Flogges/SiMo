""" Grid tests """

from src._grid import Grid

# --------------------------------------------
def test_grid_create():
    """ test grid creation() """

    grid = Grid(num_rows= 3, num_cols= 3)

    assert grid.num_cols == 3, "num_cols is not 3"
    assert grid.num_rows == 3, "num_rows is not 3"
    # --------
    grid = Grid(num_rows= 1, num_cols= 3)

    assert grid.num_cols == 3, "num_cols is not 1"
    assert grid.num_rows == 1, "num_rows is not 3"
# --------
    cell = grid.cell_at(1,0)
    assert cell is not None, "grid cell is None"
    assert cell.row_idx == 0, "grid cell.row is not 0"
    assert cell.col_idx == 1, "grid cell.col is not 1"
