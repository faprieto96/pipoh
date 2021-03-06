from abc import abstractmethod
from pyGPGO.covfunc import squaredExponential
from pyGPGO.acquisition import Acquisition
from pyGPGO.surrogates.GaussianProcess import GaussianProcess
from pyGPGO.GPGO import GPGO
from common_functions.rolling_windows_validation import rolling_windows_validation
import numpy as np




class InitialConfiguration:
    def initial_configuration(self, strategy, params=None):
        if params != None and strategy != 'CustomStrategy':
            param_hip = params
            self.optim_param = params

        if params == None:
            if strategy == 'WUBC':
                (numElements, N) = self.data.shape
                params = {'lambda_value': ('cont', [0, 1]), 'upperBound': ('cont', [1/N, 1])}
            if strategy == 'WLBC':
                (numElements, N) = self.data.shape
                params = {'lambda_value': ('cont', [0, 1]), 'upperBound': ('cont', [0, 1/N])}
            if strategy == 'MV':
                params = {'lambda_value': ('cont', [0, 1])}
            if (strategy == 'DMV') or (strategy == 'DMVY') or (strategy == 'EWMV'):
                params = {'lambda_value': ('cont', [0, 1]), 'delta_value': ('cont', [0, 1])}
            param_hip = params
            self.optim_param = params

        if strategy == 'CustomStrategy':
            for x, y in params.items():
                if x != 'f' and x != 'hp':
                    exec('self.{}=params["{}"]'.format(x, x))
            param_hip = params['hp']
            self.optim_param = params['hp']
            self.f = params.get('f')
            self.args = params.get('args')




        # Create the validation set
        self.intermediate_data = self.data[0:-self.validation_windows:, :]
        # Compute the CV windows
        # Create the optimization variable

        sexp = squaredExponential()
        gp = GaussianProcess(sexp)
        acq = Acquisition(mode='ExpectedImprovement')

        def errorLoss(*args, **kwards):
            for x,y in kwards.items():
                self.optim_param.setdefault(x,y)
                self.values = kwards
            try:
                for x, y in self.values.items():
                    if x != 'f' and x != 'hp':
                        exec('self.{}=y'.format(x, x))
            except:
                pass
            rolling_windows_validation(self)
            value = np.std(self.returns) / self.returns.mean()
            return value

        results = GPGO(gp, acq, errorLoss, param_hip)
        try:
            results.run(max_iter=1)
        except TypeError:
            pass
        # Extract the best parameters
        # obj.lambda_value = results.best[[0]]
        # obj.upperBound = results.best[[1]]
        self.values = results.getResult()

        for x, y in dict(self.values[0]).items():
            exec('self.{}={}'.format(x,y))
        # obj.lambda_value = results.getResult()
        # obj.upperBound = 0.3128
        return 'SUCCESS'

