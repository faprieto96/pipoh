from strategies.gscv_agrupacion_estrategias import *


class gscvFactory:
    @staticmethod
    def get_specific_strategy(strategy_selected, params=None):
        try:
            if strategy_selected == 'GridSearchCV'+'MV':
                return gscvMV()
            if strategy_selected == 'GridSearchCV'+'WUBC':
                return gscvWUBC()
            if strategy_selected == 'GridSearchCV'+'WLBC':
                return gscvWLBC()
            if strategy_selected == 'GridSearchCV'+'DMV':
                return gscvDMV()
            if strategy_selected == 'GridSearchCV'+'DMVY':
                return gscvDMVY()
            if strategy_selected == 'GridSearchCV'+'EWMV':
                return gscvEWMV()
            if strategy_selected == 'GridSearchCV'+'CustomStrategy':
                return gscvCUSTOM()
            raise Exception('Strategy Not Found')
        except Exception as _e:
            print(_e)
        return None
