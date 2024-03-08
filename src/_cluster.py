from ._cell import Cell

from typing import Set
from typing import Optional

# import importlib
#Grid = importlib.import_module("._grid" , package='src')

class Cluster:
    """ Full islands (not subsets thereof) of black cells """

    # ---------------------------------------------------------

    cells : Set[Cell] = set()   # using set (instead of eg List) stops duplicates from being added (by mistake)


    # used to tell if cluster percolates
    col_idx_min: int = -1  # the closer to 0, the closer to top of grid
    col_idx_max: int = -1  # the closer to (grid.num_cols)-1, the closer to top of grid
   # grid: Optional[Grid] = None

    # -------------------------------
    def __init__(self): #, grid: Grid):
    #   self.grid = grid
        pass

    # -------------------------------
    def num_cells(self) -> int:
        return len(self.cells)
    # # -------------------------------
    # def percolates(self, grid: Grid) -> bool:
    #     """ does cluster extend from top to ottom of grid? """
    #     if self.grid is None:
    #         return False
    #
    #     touches_top = self.col_idx_max == 0
    #     touches_bottom =  self.col_idx_max == (self.grid.num_rows-1)
    #
    #     return touches_top and touches_bottom

    # -------------------------------
    def add_cell(self, cell: Cell):
        if (Cell is not None) and (cell.is_black):
            self.cells.add(cell)
            self.update_col_idx(cell)

    # -------------------------------
    def update_col_idx(self, cell: Cell) -> None:
        """ updates col_idx_min/max if cell is closer to top/bottom of grid"""
        if Cell is None:
            return

        if cell.col_idx < self.col_idx_min:
            self.col_idx_min = cell.col_idx

        if cell.col_idx > self.col_idx_max:
            self.col_idx_max = cell.col_idx

# -------------------------------
