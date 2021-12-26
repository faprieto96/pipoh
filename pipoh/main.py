from pipoh.Parents.strategy_factory import StrategyFactory
from pipoh.common_functions.rolling_windows_validation import rolling_windows_validation
from pipoh.common_functions.max_drawdown import max_drawdown
from pipoh.common_functions.output_financial_ratios import output_financial_ratios
from pipoh.common_functions.classes_init import Data

#Desactivate warnings
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
#data = np.matrix(pd.read_csv(str(os.getcwd() + '/data_library/6_Emerging_Markets_8years.csv'), header=None))

#if __name__ == '__main__':

def pipoh(strategy: str, input_data: callable, optimization:str = None, params = None):
    try:
        input_data = Data.library_data(input_data=input_data)
    # The user introduces the path of .csv file
    except SyntaxError:
        input_data = Data.import_data(input_data=input_data)
    except AttributeError:
        input_data = Data.import_data(input_data=input_data)

    if optimization is None and params is None:
        STRATEGY_SELECTED = StrategyFactory.get_strategy(strategy)
        # 2. Import the data into the strategy
        STRATEGY_SELECTED.data = input_data
    if optimization is not None and params is None:
        STRATEGY_SELECTED = StrategyFactory.get_strategy(optimization+strategy)
        # 2. Import the data into the strategy
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
    STRATEGY_SELECTED.output_financial_summary = output_financial_ratios(STRATEGY_SELECTED.ratios, STRATEGY_SELECTED.returns, STRATEGY_SELECTED.weights)
    return STRATEGY_SELECTED.output_financial_summary

"""
#Ejemplo 1: Sin método de optimización de hiper-parámetros
ejemplo1 = pydiversity(strategy='EW', input_data='emerging_markets')
print(ejemplo1)

#Ejemplo 2: Incluyendo optimización de hyper-parámetros a través del método bayesiano
ejemplo2 = pydiversity(strategy='WLBC', optimization='Bayesian', input_data='emerging_markets', params={'lamb': ('cont', [0.5, 1]), 'lower_bound': ('cont', [0.8, 1])})
print(ejemplo2)

#Ejemplo 3: Incluyendo una función externa
def dominancia_estocastica(self):
    lambdaValue = self.lambda_value
    # lambdaValue = 0.886
    upperBoundValue = self.lower_bound
    return lambdaValue+upperBoundValue

params_defined = {'f': dominancia_estocastica, 'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}
ejemplo3 = pydiversity(strategy='CustomStrategy', optimization='Bayesian', input_data='emerging_markets', params=params_defined)
print(ejemplo3)


#Ejemplo 4: optimizer GridSearchCV
params_defined = {'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}
ejemplo4 = pydiversity(strategy='WLBC', optimization='GridSearchCV', input_data='emerging_markets', params=params_defined)
print(ejemplo4)

print('FINISHED SUCCESSFULLY')
"""