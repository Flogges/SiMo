from ._cell import Cell
from ._cluster import Cluster
from typing import List, Tuple, Set
from typing import Optional

Row = List[Cell]  # Alias for List (so we can use eg "List[Row]"  instead of "List[List[Cell]]" )

class Grid:
    """  Matrix of size (rows x cols) cells """

    # ---------------------------------------------------------
    num_rows: int = -1
    num_cols: int = -1

    clusters:   Set[Cluster] = set()
    rows:       List[Row] = []

    steps_taken = 0
    # ----------------------------
    # if/when percolation occurs, save the cluster responsible, and cell in it that last turned black
    perc_cluster: Optional[Cluster] = None
    perc_cell: Optional[Cell] = None

    # -------------------------------
    def perc_value(self):
        return float(self.steps_taken)/(float(self.num_cols * self.num_rows))
    # -------------------------------
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols

        for row_idx in range(num_rows):
            row = list()
            for col_idx in range(num_cols):
                cell = Cell(col_idx, row_idx, is_black=False, grid=self)
                row.append(cell)
            self.rows.append(row)

    # -------------------------------
    @classmethod
    def indices_adjacent_to(Cls, num_rows: int, num_cols: int, row_idx: int, col_idx: int) -> Optional[List[Tuple[int,int]]]:
        """ return list of cells adjacent to given cell (row_idx, col_idx) in grid of size (num_rows x num_cols) """


        deltas = [
            (-1, -1), (-1, 0), (-1, 1),  # Above row
            (0, -1), (0, 1),  # Same row
            (1, -1), (1, 0), (1, 1)  # Below row
        ]

        ret = []
        for d_row, d_col in deltas:
            adj_row, adj_col = row_idx + d_row, col_idx + d_col
            # Check if the adjacent cell is within the matrix bounds
            if 0 <= adj_row < num_rows and 0 <= adj_col < num_cols:
                ret.append((adj_row, adj_col))

        return ret
    # -------------------------------
    def cells_adjacent_to(self, row_idx: int, col_idx: int,) -> Optional[List[Cell]]:
        """ return list of cells adjacent to given cell (row_idx, col_idx) """

        cell = self.cell_at(row_idx, col_idx)
        if cell is None:
            return None

        indices = self.indices_adjacent_to(self.num_rows, self.num_cols, row_idx, col_idx)
        return self.cells_at(indices)

    # -------------------------------
    def cells_at(self, indices: Optional[List[Tuple[int, int]]]) -> Optional[List[Cell]]:

        ret: List[Cell] = []
        if indices is None:
            return ret

        for (row_idx, col_idx) in indices:
            cell = self.cell_at(row_idx, col_idx)
            if not cell is None:
                ret.append(cell)

        return ret

    # -------------------------------
    def cell_at(self, row_idx: int, col_idx: int) -> Optional[Cell]:
        """ return cell at given posn (col_idx,row_idx), or None if invalid

         order of indices: (row_idx, col_idx) -not- (col_idx, row_idx)~(x,y)
         same convention as numpy/pandas """

        # check for out of bounds (num_rows, num_cols) of grid
        if row_idx < 0 or (row_idx > self.num_rows):
            return None

        if col_idx < 0 or (col_idx > self.num_cols):
            return None
        # -------

        # check for no cell at given posn
        if row_idx > len(self.rows):
            return None
        row = self.rows[row_idx]


        if col_idx > len(row):
            return None
        cell = row[col_idx]
        return cell

    # -------------------------------
    def step(self, row_idx: int, col_idx: int) -> bool:
        """ turn cell at given posn (col_idx,row_idx) black, merge any clusters.
         return whether true if percolation has occured in this step """

        cell = self.cell_at(row_idx, col_idx)
        if cell is None:
            return False

        self.steps_taken += 1

        cell.turn_black()
        cluster = Cluster(grid=self)
        cluster.add_cell(cell)
        self.clusters.add(cluster)


        adjacent_cells = self.cells_adjacent_to(row_idx, col_idx)
        if adjacent_cells is None:
            return False

        for cell_a in adjacent_cells:
            if cell_a.is_black:
                cluster_a  = cell_a.cluster
                self.merge_clusters(cluster, cluster_a)

        perc = cluster.percolates()
        if(perc):
            self.perc_cluster = cluster
            self.perc_cell = cell

        return perc

    # -------------------------------
    def merge_clusters(self, cla: Cluster, clb: Optional[Cluster]):
        """ merge any clusters.
         return whether true if percolation has occured in this step """

        if clb is None:
            return

        cla.merge(clb)
        self.clusters.remove(clb)
