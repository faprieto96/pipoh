import numpy as np
from sklearn.covariance import EmpiricalCovariance
from qpsolvers import solve_qp

from abc import ABCMeta, abstractmethod, ABC

class fnc_WLBC(ABC):
    __metaclass__ = ABCMeta
    def __init__(self, name='Weighted lower Bound Constraint, WUBC', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12) -> None:
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
        # Type: It returns the optimized weights
        # Compute numbers of data points and assets
        try:
            self.optim_param = eval(self.optim_param)
        except:
            pass
        lambdaValue=self.optim_param.get('lambda_value')
        (numElements, N) = self.intermediate_data.shape
        # mean and covariance
        assert np.count_nonzero(np.isnan(self.intermediate_data)) == 0
        if len(self.intermediate_data)==0:
            pass

        Sigma = np.cov(self.intermediate_data, rowvar=False)* 12  # I use 12 for annualizing the covmatrix
        Vars = np.diag(Sigma)  # variances of the stocks
        mu = self.intermediate_data.mean(axis=0).H * 12  # mean log returns

        lambdaValue = self.lamb
        # lambdaValue = 0.886
        lowerBoundValue = self.lower_bound
        # lowerBoundValue = 0
        H = 2 * (lambdaValue * Sigma)
        f = - mu.H

        if len(f)==0:
            try:
                q_p = np.asarray(f).reshape((6,))
            except:
                q_p = np.zeros((1, N)).reshape((6,))
        if len(f)>0:
            q_p = np.array(- mu.H)[0]

        Aeq = np.ones((1, N)).reshape(6)
        beq = np.array(1)
        LB = (np.ones((1, N))* lowerBoundValue)[0]
        UB = np.ones((1, N)).reshape(6,)

        # Python reference for quadprog:
        #   https://pypi.org/project/qpsolvers/
        # Original funct (it contains opts) (Wa, varP)  = solve_qp(H,f,[],[],Aeq,beq,LB,UB,UB/N,opts)

        W=np.asarray(solve_qp(P = H, q = q_p, G = None, h = None, A = Aeq, b = beq, lb = LB, ub = UB))

        return W
