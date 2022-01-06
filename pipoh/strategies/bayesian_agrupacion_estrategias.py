# Fichero que contiene la agrupación de todas las estrategias.
from concrete_factories.bayesian_folder.bayesian_interface import InterfaceBayesian
from strategies.individual_strategies.class_wlbc import fnc_WLBC
from strategies.individual_strategies.class_wubc import fnc_WUBC
from strategies.individual_strategies.class_mv import fnc_MV
from strategies.individual_strategies.class_dmv import fnc_DMV
from strategies.individual_strategies.class_dmvy import fnc_DMVY
from strategies.individual_strategies.class_ewmv import fnc_EWMV
from strategies.individual_strategies.class_custom import fnc_CUSTOM

# Se importan las funciones, dentro de la clase que ejecutará.
# Es el método común de importar todas las funciones a partir de un fichero común de python.
# Todo proviene de la carpeta pipoh > strategies. Por lo que la función se modificaría en todas las carpetas.


class bayesianWLBC(fnc_WLBC, InterfaceBayesian):
    def __init__(self):
        super(bayesianWLBC, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianWLBC, self).solve_optimization_problem()


class bayesianWUBC(fnc_WUBC, InterfaceBayesian):
    def __init__(self):
        super(bayesianWUBC, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianWUBC, self).solve_optimization_problem()


class bayesianMV(fnc_MV, InterfaceBayesian):
    def __init__(self):
        super(bayesianMV, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianMV, self).solve_optimization_problem()

class bayesianDMV(fnc_DMV, InterfaceBayesian):
    def __init__(self):
        super(bayesianDMV, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianDMV, self).solve_optimization_problem()

class bayesianDMVY(fnc_DMVY, InterfaceBayesian):
    def __init__(self):
        super(bayesianDMVY, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianDMVY, self).solve_optimization_problem()

class bayesianEWMV(fnc_EWMV, InterfaceBayesian):
    def __init__(self):
        super(bayesianEWMV, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianEWMV, self).solve_optimization_problem()

class bayesianCUSTOM(fnc_CUSTOM, InterfaceBayesian):
    def __init__(self):
        super(bayesianCUSTOM, self).__init__()

    def solve_optimization_problem(self):
        return super(bayesianCUSTOM, self).solve_optimization_problem()
