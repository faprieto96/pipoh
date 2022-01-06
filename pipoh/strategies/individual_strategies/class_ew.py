import numpy as np

from abc import ABCMeta, abstractmethod, ABC

class fnc_EW(ABC):
    __metaclass__=ABCMeta
    def __init__(self, name='Equally Weighted Strategy, EW', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12) -> None:
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
        """
        Equally Weighted Strategy
        :param data_received:
        :param parameters:
        :param optimization:
        :return: It returns the optimized weights
        """
        name = 'Equally Weighted Strategy'

        (numElements, N) = self.intermediate_data.shape
        # mean and covariance

        weights = np.ones((N, 1)) * (1 / N)
        self.weights = weights

        return self.weights
