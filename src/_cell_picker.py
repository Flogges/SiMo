


import random
from typing import List, Tuple


class CellPicker:
    """ Sequence of cells in (random) order from (num_rows x num_cols) sized grid"""

    # ---------------------------------------------------------
    num_rows:    int = -1
    num_cols:    int = -1

    # -------------------------------
    def __init__(self, num_rows, num_cols):
        """ order of indices: (row_idx, col_idx) -not- (col_idx, row_idx)~(x,y)
           same convention as numpy/pandas """
        self.num_rows = num_rows
        self.num_cols = num_cols

    # -------------------------------
    def seq_random(self, deterministic=False) -> List[Tuple[int,int]]:
        """ return random sequence of cells.
        if deterministic is true, then returns the same sequence every time. """

        # Generate a list of all cell indices
        indices = [(row, col) for row in range(self.num_rows) for col in range(self.num_cols)]

        if(deterministic):
            random.seed(42)
        # Shuffle the indices list in-place to ensure a different order each time
        random.shuffle(indices)

        return indices

# -------------------------------
