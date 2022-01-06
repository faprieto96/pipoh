import numpy as np

from abc import ABCMeta, abstractmethod, ABC

class fnc_GMR(ABC):
    __metaclass__ = ABCMeta
    def __init__(self, name='Global Maximum Return Strategy, GMR', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12) -> None:
        self.name = name
        self.lamb = lamb
        self.delta = delta
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.validation_windows = validation_windows
        self.cv_windows = cv_windows
        self.data = []
        self.intermediate_data = []
        self.weights = []
        self.returns = []
        self.optim_param = {}

    @abstractmethod
    def solve_optimization_problem(self):

        (numElements, N) = self.intermediate_data.shape
        # Compute the mean return
        # meanReturn  =
        meanReturn = self.intermediate_data.mean(axis=0)
        # Global maximun return approach
        ValueMax = meanReturn.max()
        indexMax = list(np.where(meanReturn == meanReturn.max()))[1][0]
        W = np.zeros((N, 1))
        W[[indexMax]] = 1

        return W





