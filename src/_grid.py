from ._cell import Cell
from ._cluster import Cluster
from typing import List


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

    def cell_at(col_idx, row_idx):
       pass
