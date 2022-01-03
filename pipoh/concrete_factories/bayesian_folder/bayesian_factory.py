from pipoh.concrete_factories.bayesian_folder.bayesian_strategies.bayesian_custom import BayesianCustomStrategy
from pipoh.strategies.bayesian_agrupacion_estrategias import *

class BayesianFactory:
    """The Factory Class"""

    @staticmethod
    def get_specific_strategy(strategy_selected, params=None):
        """A static method to get a chair"""
        try:
            if strategy_selected == 'BayesianMV':
                return bayesianMV()
            if strategy_selected == 'BayesianWUBC':
                return bayesianWUBC()
            if strategy_selected == 'BayesianWLBC':
                return bayesianWLBC()
            if strategy_selected == 'BayesianDMV':
                return bayesianDMV()
            if strategy_selected == 'BayesianDMVY':
                return bayesianDMVY()
            if strategy_selected == 'BayesianEWMV':
                return bayesianEWMV()
            if strategy_selected == 'BayesianCustomStrategy':
                return bayesianCUSTOM()
            raise Exception('Strategy Not Found')
        except Exception as _e:
            print(_e)
        return None
