from strategies.non_parametric_agrupacion_estrategias import *

class NonParametricFactory:

    @staticmethod
    def get_specific_strategy(strategy_selected, params=None):
        """A static method to get a chair"""
        try:
            if strategy_selected == 'EW':
                return non_parameteric_EW()
            if strategy_selected == 'GMR':
                return non_parameteric_GMR()
            if strategy_selected == 'GMV':
                return non_parameteric_GMV()
            if strategy_selected == 'CustomStrategy':
                return non_parameteric_CUSTOM()
            raise Exception('Strategy not found')
        except Exception as _e:
            print(_e)
        return None
