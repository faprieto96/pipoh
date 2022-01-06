import numpy as np
from sklearn.covariance import EmpiricalCovariance
#from qpsolvers import solve_qp

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

        try:
            Sigma = EmpiricalCovariance().fit(self.intermediate_data).covariance_ * 12  # I use 12 for annualizing the covmatrix
        except:
            pass
        # mean log returns

        H = 2 * Sigma
        f = []  # FALTA TRANSPOSE

        Aeq = np.ones((1, N))
        beq = 1
        LB = np.zeros((1, N))
        UB = np.ones((1, N))
        # opts    = optimset('Algorithm', 'interior-point-convex', 'Display','off')
        #   Revisar cómo meter la opción de 'interior-point-convex'

        # Python reference for quadprog:
        #   https://pypi.org/project/qpsolvers/
        # Original funct (it contains opts) (Wa, varP)  = solve_qp(H,f,[],[],Aeq,beq,LB,UB,UB/N,opts)

        P = H
        try:
            q = np.asarray(f).reshape((6,))
        except:
            q = np.zeros((1, N)).reshape((6,))
        G = np.zeros((6, 6))
        h = np.zeros(6)
        A = np.asarray(Aeq).reshape((6,))
        b = np.array([beq])
        lb = LB
        ub = UB



        """M = array([[1., 2., 0.], [-8., 3., 2.], [0., 1., 1.]])
        P = dot(M.T, M)  # this is a positive definite matrix
        q = dot(array([3., 2., 3.]), M).reshape((3,))
        G = array([[1., 2., 1.], [2., 0., 1.], [-1., 2., -1.]])
        h = array([3., 2., -2.]).reshape((3,))
        A = array([1., 1., 1.])
        b = array([1.])"""

        # (Wa, varP, third_parameter) = solve_qp(P, q, G, h, A, b)

        # (Wa, varP, third_parameter,fourth_parameter,fifth_parameter,sixt_parameter)  = solve_qp(P, q, G, h, A, b)
        #W = np.array(solve_qp(P, q, G, h, A, b))
        # W = deltaValue* Wa + (1-deltaValue)*(1/N)*np.ones((N,1))
        W = np.ones((6, 1))

        return W





