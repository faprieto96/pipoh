"""Abstract Strategy Factory"""
from Parents.interface_strategy_factory import InterfaceStrategyFactory
from concrete_factories.bayesian_folder.bayesian_factory import BayesianFactory
from concrete_factories.non_parametric.non_parametric_factory import NonParametricFactory
from concrete_factories.gscv_folder.gscv_factory import gscvFactory

# Modificar y poner o 1) Clases y sino 2) sets.
list_non_parametric_strategies = ['GMR', 'GMV', 'EW', 'EWRC', 'MD']
list_bayesian_strategies = ['BayesianMV', 'BayesianWUBC', 'BayesianWLBC', 'BayesianDMV', 'BayesianDMVY', 'BayesianEWMV',
                            'BayesianCustomStrategy']
list_gscv_strategies = ['GridSearchCVMV', 'GridSearchCVWUBC', 'GridSearchCVWLBC', 'GridSearchCVDMV', 'GridSearchCVDMVY',
                        'GridSearchCVEWMV', 'GridSearchCVCustomStrategy']


class StrategyFactory(InterfaceStrategyFactory):
    """The Abstract Factory Concrete Class"""
    @staticmethod
    def get_strategy(strategy_selected, params=None):
        """Static get_factory method"""
        try:
            if strategy_selected in list_bayesian_strategies:
                return BayesianFactory.get_specific_strategy(strategy_selected, params)
            if strategy_selected in list_non_parametric_strategies:
                return NonParametricFactory.get_specific_strategy(strategy_selected)
            if strategy_selected in list_gscv_strategies:
                return gscvFactory.get_specific_strategy(strategy_selected, params)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None

    @staticmethod
    def initial_configuration(strategy_selected, params=None):
        """Static get_factory method"""
        try:
            if strategy_selected in list_bayesian_strategies:
                return BayesianFactory.get_specific_strategy(strategy_selected, params)
            if strategy_selected in list_non_parametric_strategies:
                return NonParametricFactory.get_specific_strategy(strategy_selected)
            if strategy_selected in list_gscv_strategies:
                return gscvFactory.get_specific_strategy(strategy_selected, params)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
