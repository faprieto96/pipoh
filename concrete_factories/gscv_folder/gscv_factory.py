from concrete_factories.gscv_folder.gscv_strategies.gscv_wlbc import gscvWLBC


class gscvFactory:
    """The Factory Class"""

    @staticmethod
    def get_specific_strategy(strategy_selected, params=None):
        """A static method to get a chair"""
        try:
            if strategy_selected == 'GridSearchCVWLBC':
                return gscvWLBC()
            raise Exception('Strategy Not Found')
        except Exception as _e:
            print(_e)
        return None
