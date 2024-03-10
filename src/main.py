
from src._experiment import Experiment
from typing import List
import time

# --------------------------------------------
def calculate_p_av(num_rows: int = 30, num_cols: int =30, batch_size: int = 30 ) -> float :


    """
    :return:            average proportion of grid cells that must be turned on before percolation occurs


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
    print(f"...average p: {p_av} with ({num_rows}x{num_cols}) grid, {batch_size} iterations in {round(time_delta,2)} secs ")
    return p_av
# --------------------------------------------
if __name__ == "__main__" :
    calculate_p_av(num_rows=50, num_cols=50, batch_size=50)
