""" Experiment tests """

from src._experiment import Experiment

# --------------------------------------------
def test_experiment():
    """ Run an experiment """

    p = Experiment().do_it()
    assert 0 <p < 1

# --------------------------------------------
