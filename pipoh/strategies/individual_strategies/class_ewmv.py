import numpy as np
from sklearn.covariance import EmpiricalCovariance
from qpsolvers import solve_qp

from abc import ABCMeta, abstractmethod, ABC

class fnc_EWMV(ABC):
    __metaclass__ = ABCMeta
    def __init__(self, name='Diversified Mean Variance Strategy, DMV', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12) -> None:
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
        # mean and covariance
        try:
            Sigma = np.cov(self.intermediate_data, rowvar=False)* 12  # I use 12 for annualizing the covmatrix
        except:
            pass
        Vars = np.diag(Sigma)  # variances of the stocks
        mu = self.intermediate_data.mean(axis=0).H * 12  # mean log returns

        try:
            self.optim_param = eval(self.optim_param)
        except:
            pass

        try:
            if type(self.lambda_value) == float:
                lambdaValue = self.lambda_value
                deltaValue = self.delta_value
            if type(self.optim_param.get('lambda_value')) == float:
                lambdaValue = self.optim_param.get('lambda_value')
                deltaValue = self.optim_param.get('delta_value')
        except:
            pass

        try:
            lambdaValue+1
        except:
            try:
                lambdaValue = self.lambda_value
                deltaValue = self.delta_value
            except:
                lambdaValue = self.optim_param.get('lambda_value')
                deltaValue = self.optim_param.get('delta_value')

        H = 2 * (lambdaValue * Sigma + deltaValue * np.eye(N))
        f = - mu.H

        if len(f)==0:
            try:
                q_p = np.asarray(f).reshape((6,))
            except:
                q_p = np.zeros((1, N)).reshape((6,))
        if len(f)>0:
            q_p = np.array(f)[0]

        Aeq = np.ones((1, N)).reshape(6)
        beq = np.array(1)
        LB = np.zeros((1, N))[0]
        UB = np.ones((1, N)).reshape(6,)

        # Python reference for quadprog:
        #   https://pypi.org/project/qpsolvers/
        # Original funct (it contains opts) (Wa, varP)  = solve_qp(H,f,[],[],Aeq,beq,LB,UB,UB/N,opts)

        Wa = np.asarray(solve_qp(P = H, q = q_p, G = None, h = None, A = Aeq, b = beq, lb = LB, ub = UB))
        W = deltaValue* Wa + (1-deltaValue)*(1/N)*np.ones((6,1)).reshape(6)

        return W





