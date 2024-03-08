

from typing import Optional
#import importlib

# At the module level, dynamically import the Cluster class from _cluster.py
#Cluster = importlib.import_module('._cluster', package='src').Cluster
#Cluster = importlib.import_module("._cluster" , package='src')


class Cell:
    """ Smallest individual 'unit' of a grid. Has indices (x,y) and color"""

    # ---------------------------------------------------------
    col_idx:    int = -1      # ~x-coordinate
    row_idx:    int  = -1     # ~y-coordinate
    is_black:   bool = False
   # cluster:    Optional[Cluster] = None

    # -------------------------------
    def __init__(self, col_idx, row_idx):
        self.col_idx = col_idx
        self.row_idx = row_idx

# -------------------------------
#from ._cluster import Cluster
