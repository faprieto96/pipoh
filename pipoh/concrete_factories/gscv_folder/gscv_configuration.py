import numpy as np
from sklearn.base import BaseEstimator
from sklearn.model_selection import GridSearchCV
from pipoh.common_functions.rolling_windows_validation import rolling_windows_validation

class custom_gridsearch_cv(BaseEstimator):

    def __init__(self,  STRATEGY_SELECTED):
        self.STRATEGY_SELECTED = STRATEGY_SELECTED
        """try:
            for x, y in self.param_grid.items():
                if x != 'f' and x != 'hp':
                    exec('self.{}=y'.format(x, x))
        except:
            pass"""
        return

    def fit(self, X, STRATEGY_SELECTED):
        STRATEGY_SELECTED.intermediate_data = X
        try:
            STRATEGY_SELECTED.optim_param=self.optim_param
        except:
            pass
        rolling_windows_validation(STRATEGY_SELECTED)
        value = np.std(STRATEGY_SELECTED.returns) / STRATEGY_SELECTED.returns.mean()
        return value

    """def get_params(self, deep=True):
        return {"n_nodes": self.n_nodes,
                "n_jobs": self.n_jobs}"""

    def set_params(self, **parameters):
        array_values = []
        for parameter, value in parameters.items():
            setattr(self, parameter, value)
            array_values.append("'" + str(parameter) + "' : "+ str(value))
        self.optim_param = "{"+', '.join(array_values)+"}"

        return self

"""### Fit the c parameter ###
X = np.random.normal(0, 1, (100,5))
y = X[:,1] * X[:,2] + np.random.normal(0, .1, 100)

gs = GridSearchCV(custom_gridsearch_cv(n_nodes=20), cv=5, param_grid={"c":np.linspace(0.0001,1,10)}, scoring = 'accuracy')
output = gs.fit(X)
output.best_params_"""



class InitialConfiguration(custom_gridsearch_cv):
    def initial_configuration(self, strategy, params=None):

        if params == None:
            if strategy == 'WUBC':
                (numElements, N) = self.data.shape
                params = {'lambda_value': ('cont', [0, 1]), 'upperBound': ('cont', [1/N, 1])}
            if strategy == 'WLBC':
                (numElements, N) = self.data.shape
                params = {'lambda_value': ('cont', [0, 1]), 'upperBound': ('cont', [0, 1/N])}
            if strategy == 'MV':
                params = {'lambda_value': ('cont', [0, 1])}
            if ((strategy == 'DMV') or (strategy == 'DMVY') or (strategy == 'EWMV')):
                params = {'lambda_value': ('cont', [0, 1]), 'delta_value': ('cont', [0, 1])}
            param_hip = params
            self.optim_param = params

        if strategy == 'CustomStrategy':
            for x, y in params.items():
                if x!='f' and x!='hp':
                    exec('self.{}=params["{}"]'.format(x, x))
            param_hip = params['hp']
            self.optim_param = params['hp']
            self.f = params.get('f')
            self.args = params.get('args')


        if strategy != 'CustomStrategy':
            try:
                for x, y in params.items():
                    if x != 'f' and x != 'hp':
                        exec('self.{}=params["{}"]'.format(x, x))
                param_hip = params['hp']
                self.optim_param = params['hp']
            except:
                param_hip = params
                self.optim_param = params

        try:
            for x, y in self.values.items():
                if x != 'f' and x != 'hp':
                    exec('self.{}=y'.format(x, x))
        except:
            pass

        array_values=[]
        for x, y in self.optim_param.items():
            array_values.append("'"+str(x)+"'"+": np.linspace("+str(self.optim_param[x][1][0]) + ", "+str(self.optim_param[x][1][1])+ ", 10"+")")
        parameters_in_gscv=', '.join(array_values)
        print('{'+parameters_in_gscv+'}')
        self.optim_param = eval('{'+parameters_in_gscv+'}')


        gs = GridSearchCV(custom_gridsearch_cv( STRATEGY_SELECTED = self), cv=5, param_grid=self.optim_param, scoring = 'accuracy')
        output = gs.fit(self.data[0:-self.validation_windows:, :], STRATEGY_SELECTED=self)
        output.best_params_

        # Extract the best parameters
        # obj.lambda_value = results.best[[0]]
        # obj.upperBound = results.best[[1]]
        #self.values = results.getResult()

        for x, y in output.best_params_.items():
            exec('self.{}={}'.format(x,y))
        # obj.lambda_value = results.getResult()
        # obj.upperBound = 0.3128
        return 'SUCCESS'







