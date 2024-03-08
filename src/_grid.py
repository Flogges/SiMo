from ._cell import Cell
from ._cluster import Cluster
from typing import List
from typing import Optional

Row = List[Cell]  # Alias for List (so we can use eg "List[Row]"  instead of "List[List[Cell]]" )

class Grid:
    """  Matrix of size (rows x cols) cells """

    # ---------------------------------------------------------
    num_rows: int = -1
    num_cols: int = -1

    clusters:   List[Cluster] = []
    rows:       List[Row] = []

    # -------------------------------
    def __init__(self, num_rows, num_cols):
        self.rows = num_rows
        self.cols = num_cols

        for row_idx in range(num_rows):
            row = Row()
            for col_idx in range(num_cols):
                cell = Cell(col_idx, row_idx)
                row.append(cell)
            self.rows.append(Row)

    # -------------------------------
    def cell_at(self, col_idx: int, row_idx: int) -> Optional[Cell]:
        """ return cell at given posn (col_idx,row_idx), or None if invalid"""

        # check for out of bounds (num_rows, num_cols) of grid
        if row_idx < 0 or (row_idx > self.num_rows):
           return None

        if col_idx < 0 or (col_idx > self.num_cols):
            return None
        # -------

        # check for no cell at given posn
        if(row_idx > len(self.rows)):
            return None
        row = self.rows[row_idx]


        if (col_idx > len(row)):
            return None
        Cell = row[col_idx]
        return Cell
