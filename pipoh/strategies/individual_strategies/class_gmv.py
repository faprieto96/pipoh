import numpy as np
from sklearn.covariance import EmpiricalCovariance
from qpsolvers import solve_qp

from abc import ABCMeta, abstractmethod, ABC

class fnc_GMV(ABC):
    __metaclass__ = ABCMeta
    def __init__(self, name='Global Minimum Variance Strategy, GMV', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12) -> None:
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

        Sigma = np.cov(self.intermediate_data, rowvar=False)* 12  # I use 12 for annualizing the covmatrix

        # mean log returns

        H = 2 * Sigma
        f = []  # FALTA TRANSPOSE

        try:
            q_p = np.asarray(f).reshape((6,))
        except:
            q_p = np.zeros((1, N)).reshape((6,))

        Aeq = np.ones((1, N)).reshape(6)
        beq = np.array(1)
        LB = np.zeros((1, N)).reshape(6,)
        UB = np.ones((1, N)).reshape(6,)

        # Python reference for quadprog:
        #   https://pypi.org/project/qpsolvers/
        # Original funct (it contains opts) (Wa, varP)  = solve_qp(H,f,[],[],Aeq,beq,LB,UB,UB/N,opts)

        W=np.asarray(solve_qp(P = H, q = q_p, G = None, h = None, A = Aeq, b = beq, lb = LB, ub = UB))
        #W = np.array(solve_qp(P, q, G, h, A, b))
        #W = deltaValue* Wa + (1-deltaValue)*(1/N)*np.ones((N,1))
        #W = np.ones((6, 1))

        return W





