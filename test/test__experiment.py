""" Experiment tests """

from src._experiment import Experiment

# --------------------------------------------
def test_experiment():
    """ Run an experiment """

    p = Experiment().do_it(num_rows=3, num_cols=3)
    assert 0 <p < 1

# --------------------------------------------
