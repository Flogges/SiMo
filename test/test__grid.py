""" Grid tests """

from src._grid import Grid

# --------------------------------------------
def test_grid_create():
    """ test test_grid creation() """

    grid = Grid(num_rows= 3, num_cols= 3)

    assert grid.num_cols == 3, "num_cols is not 3"
    assert grid.num_rows == 3, "num_rows is not 3"
