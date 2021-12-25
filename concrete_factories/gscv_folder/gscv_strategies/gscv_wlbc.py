from concrete_factories.gscv_folder.gscv_interface import InterfaceGSCV
from concrete_factories.gscv_folder.gscv_strategies.bayesian_common_functions import test_fcn
from strategies.class_wlbc import fnc_WLBC

class gscvWLBC(fnc_WLBC, InterfaceGSCV):

    def __init__(self, name='Weighted lower Bound Constraint, WUBC', lamb=1, delta=1, upper_bound=1, lower_bound=0, validation_windows=36, cv_windows=12):
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

    def get_dimensions(self):
        return {
            "Strategy Name": self.name,
            "Lambda initial value": self.lamb,
            "Upper bound limit initial value": self.upper_bound
        }

    def get_all_parameters(self):
        return {
            "Strategy Name": self.name,
            "Lambda initial value": self.lamb,
            "Upper bound limit initial value": self.upper_bound,
            "CV windows": self.cv_windows
        }

    def get_hyper_parameters(self):

        return test_fcn(self.lamb, self.delta)

    def solve_optimization_problem(self):
        return super(gscvWLBC, self).solve_optimization_problem()
