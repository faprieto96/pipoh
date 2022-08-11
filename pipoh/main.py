from Parents.strategy_factory import StrategyFactory
from common_functions.rolling_windows_validation import rolling_windows_validation
from common_functions.max_drawdown import max_drawdown
from common_functions.output_financial_ratios import output_financial_ratios
from common_functions.data_import import Data

#Desactivate warnings
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
#data = np.matrix(pd.read_csv(str(os.getcwd() + '/data_library/6_Emerging_Markets_8years.csv'), header=None))

#if __name__ == '__main__':

def pipoh(strategy: str, input_data: callable, optimization:str = None, params = None):

    input_data = Data(data_requested=input_data).import_data()

    if optimization is None and params is None:
        STRATEGY_SELECTED = StrategyFactory.get_strategy(strategy)
        STRATEGY_SELECTED.data = input_data
    if optimization is not None and params is None:
        STRATEGY_SELECTED = StrategyFactory.get_strategy(optimization+strategy)
        STRATEGY_SELECTED.data = input_data
        STRATEGY_SELECTED.initial_configuration(strategy)
    if optimization is not None and params is not None:
        STRATEGY_SELECTED = StrategyFactory.get_strategy(optimization + strategy, params)
        STRATEGY_SELECTED.data = input_data
        STRATEGY_SELECTED.initial_configuration(strategy, params)

    # 3. Solve the optimization problem
    rolling_windows_validation(STRATEGY_SELECTED)
    # 4. Maxdrawdown function
    STRATEGY_SELECTED.ratios = max_drawdown(STRATEGY_SELECTED)
    # 5. Output financial ratios
    STRATEGY_SELECTED.output_financial_summary = output_financial_ratios(STRATEGY_SELECTED)

    #En la parte del return, se podría incluir una nueva función que generase algo tipo report.
    return STRATEGY_SELECTED.output_financial_summary

#"""
#Ejemplo 1: Sin método de optimización de hiper-parámetros

ejemplo1_1 = pipoh(strategy='EW', input_data='/Users/franciscoantonioprietorodriguez/Documents/Git_repositories/pyInvestment/pipoh/data_library/6_Emerging_Markets_8years.csv')
print(ejemplo1_1)

ejemplo1_2 = pipoh(strategy='EW', input_data='emerging_markets')
print(ejemplo1_2)

# Ejemplo 1: Sin método de optimización de hiper-parámetros
ejemplo1_3 = pipoh(strategy='GMR', input_data='emerging_markets')
print(ejemplo1_3)

# Ejemplo 1: Sin método de optimización de hiper-parámetros
ejemplo1_4 = pipoh(strategy='GMV', input_data='emerging_markets')
print(ejemplo1_4)

#Ejemplo 2.1: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo_2_1 = pipoh(strategy='WLBC', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_1)

# Ejemplo 2.2: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo_2_2 = pipoh(strategy='MV', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_2)

# Ejemplo 2.3: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo_2_3 = pipoh(strategy='DMV', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_3)

# Ejemplo 2.4: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo_2_4 = pipoh(strategy='DMVY', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_4)

#Ejemplo 2.2: Incluyendo optimización de hyper-parámetros a través del método bayesiano
"""ejemplo_2_5 = pipoh(strategy='WUBC', optimization='Bayesian', input_data='emerging_markets', params={'lamb': ('cont', [0, 1]), 'upper_bound': ('cont', [0, 1])})
print(ejemplo_2_5)"""

# Ejemplo 2.5: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo_2_6 = pipoh(strategy='EWMV', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_6)

ejemplo_2_7= pipoh(strategy='EWMV', optimization='Bayesian', input_data='emerging_markets')
print(ejemplo_2_7)




#Ejemplo 3: Incluyendo una función externa
def dominancia_estocastica(self):
    lambdaValue = self.lambda_value
    # lambdaValue = 0.886
    upperBoundValue = self.lower_bound
    return lambdaValue+upperBoundValue

params_defined = {'f': dominancia_estocastica, 'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}



ejemplo3 = pipoh(strategy='CustomStrategy', optimization='Bayesian', input_data='emerging_markets', params=params_defined)
print(ejemplo3)




#Ejemplo 4: optimizer GridSearchCV
params_defined = {'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}
ejemplo4 = pipoh(strategy='WLBC', optimization='GridSearchCV', input_data='emerging_markets', params=params_defined)
print(ejemplo4)

params_defined = {'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}
ejemplo5 = pipoh(strategy='WUBC', optimization='GridSearchCV', input_data='emerging_markets', params=params_defined)
print(ejemplo5)

params_defined = {'hp': {'lambda_value': ('cont', [0, 1])}, 'validation_windows':12}
ejemplo6 = pipoh(strategy='MV', optimization='GridSearchCV', input_data='emerging_markets', params=params_defined)
print(ejemplo6)


#Ejemplo 2.1: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2_1 = pipoh(strategy='WLBC', optimization='GridSearchCV', input_data='emerging_markets')
print(ejemplo2_1)

# Ejemplo 2.2: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2_2 = pipoh(strategy='MV', optimization='GridSearchCV', input_data='emerging_markets')
print(ejemplo2_2)

# Ejemplo 2.3: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2_3 = pipoh(strategy='DMV', optimization='GridSearchCV', input_data='emerging_markets')
print(ejemplo2_3)

# Ejemplo 2.4: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2_4 = pipoh(strategy='DMVY', optimization='GridSearchCV', input_data='emerging_markets')
print(ejemplo2_4)

# Ejemplo 2.5: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2_5 = pipoh(strategy='EWMV', optimization='GridSearchCV', input_data='emerging_markets')
print(ejemplo2_5)


#"""
#Ejemplo 7: Incluyendo una función externa con GridSearchCV
def dominancia_estocastica(self):
    try:
        self.optim_param = eval(self.optim_param)
    except:
        pass
    lambdaValue = self.optim_param['lambda_value']
    # lambdaValue = 0.886
    upperBoundValue = self.optim_param['lower_bound']
    return lambdaValue+upperBoundValue

params_defined = {'f': dominancia_estocastica, 'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}
ejemplo7 = pipoh(strategy='CustomStrategy', optimization='GridSearchCV', input_data='emerging_markets', params=params_defined)
print(ejemplo7)

print('FINISHED SUCCESSFULLY')
