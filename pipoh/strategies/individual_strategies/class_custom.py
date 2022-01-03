import numpy as np
from sklearn.covariance import EmpiricalCovariance
#from qpsolvers import solve_qp

from abc import ABCMeta, abstractmethod, ABC

class fnc_CUSTOM(ABC):
    __metaclass__ = ABCMeta
    # En el init poner los parametros que quiera
    def __init__(self):
        pass

    def get_dimensions(self):
        return 'ok'

    def get_all_parameters(self):
        return "ok"

    def get_hyper_parameters(self):
        return "Hyper parameters selection done"

    def solve_optimization_problem(self):
        try:
            for x, y in self.values.items():
                if x != 'f' and x != 'hp':
                    exec('self.{}=y'.format(x, x))
        except:
            pass
        try:
            for x, y in self.values.items():
                if x == 'f':
                    exec('self.{}=y'.format(x, x))
        except:
            pass
        self.f(self)
        return 1
