

from typing import Optional


# keep mypy happy, without actually importing (and thereby creating circular dependency  cluster <-> cell)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
     from ._cluster import Cluster
     from ._grid import Grid
     # if needs be could ue syntax like this locally
     # import importlib
     # Cluster = importlib.import_module('._cluster', package='src').Cluster


class Cell:
    """ Smallest individual 'unit' of a grid. Has indices (x,y) and color"""

    # ---------------------------------------------------------
    row_idx:    int = -1     # ~y-coordinate
    col_idx:    int = -1      # ~x-coordinate
    is_black:   bool = False
    cluster:    'Optional[Cluster]' = None
    grid:       'Optional[Grid]' = None

    # -------------------------------
    def turn_black(self, on=True):
        self.is_black = on

    # -------------------------------
    def __init__(self, row_idx, col_idx, is_black=False, grid=None):
        """ order of indices: (row_idx, col_idx) -not- (col_idx, row_idx)~(x,y)
           same convention as numpy/pandas """
        self.col_idx = col_idx
        self.row_idx = row_idx
        self.is_black = is_black
        self.grid = grid

# -------------------------------
