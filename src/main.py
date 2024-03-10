
from src._experiment import Experiment
from typing import List
import time
from src._grid_visual import visualize_as_histogram

from dataclasses import dataclass

# --------------------------------------------
@dataclass
class PercResult:
    """ Encapsulates all data in calculation """
    # in:
    num_cols:   float
    num_rows:   float
    batch_size: int

    # out:
    ps: List[float]         # p-values
    p_av:   float           # average p-value
    time_delta: float       # num of secs required to perform calculation

# --------------------------------------------
def calculate_p_av(num_rows: int = 30, num_cols: int =30, batch_size: int = 30 ) -> PercResult :
    """
    :return:            PercResult with ps, p_av, time_delta calculated


    :param num_rows:    height of grid
    :param num_cols:    width of grid
    :param batch_size:  num of individual values of p used to calculate average
    """

    t0 = time.time()

    ps: List[float] = []
    for i in range(batch_size):
        p_i= Experiment().do_it(num_rows=num_rows, num_cols=num_cols)
        ps.append(float(p_i))

    p_av = sum(ps) / float(len(ps))
    t1 = time.time()

    time_delta = t1 - t0


    result =  PercResult(num_rows=num_rows, num_cols=num_cols, batch_size=batch_size, ps=ps, p_av=p_av, time_delta=round(time_delta,2))
    return result
# ------------------------------------------------------------------
if __name__ == "__main__":

    num_rows = 100
    num_cols = 100
    batch_size= 300

    res = calculate_p_av(num_rows=num_rows, num_cols=num_cols, batch_size=batch_size)

    print(f"...average p: {res.p_av} with ({num_rows}x{num_cols}) grid, {batch_size} iterations in {res.time_delta} secs ")

    visualize_as_histogram(res.ps, x_label="p", title= f"Percolation in {batch_size} ({num_rows}x{num_cols}) grids")
