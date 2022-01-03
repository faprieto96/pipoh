# Fichero que contiene la agrupación de todas las estrategias.

from pipoh.concrete_factories.gscv_folder.gscv_interface import InterfaceGSCV

from pipoh.strategies.individual_strategies.class_mv import fnc_MV
from pipoh.strategies.individual_strategies.class_wlbc import fnc_WLBC
from pipoh.strategies.individual_strategies.class_wubc import fnc_WUBC
from pipoh.strategies.individual_strategies.class_dmv import fnc_DMV
from pipoh.strategies.individual_strategies.class_dmvy import fnc_DMVY
from pipoh.strategies.individual_strategies.class_ewmv import fnc_EWMV
from pipoh.strategies.individual_strategies.class_custom import fnc_CUSTOM

# Se importan las funciones, dentro de la clase que ejecutará.
# Es el método común de importar todas las funciones a partir de un fichero común de python.
# Todo proviene de la carpeta pipoh > strategies. Por lo que la función se modificaría en todas las carpetas.


class gscvMV(fnc_MV, InterfaceGSCV):
    def __init__(self):
        super(gscvMV, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvMV, self).solve_optimization_problem()


class gscvWLBC(fnc_WLBC, InterfaceGSCV):
    def __init__(self):
        super(gscvWLBC, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvWLBC, self).solve_optimization_problem()


class gscvWUBC(fnc_WUBC, InterfaceGSCV):
    def __init__(self):
        super(gscvWUBC, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvWUBC, self).solve_optimization_problem()


class gscvDMV(fnc_DMV, InterfaceGSCV):
    def __init__(self):
        super(gscvDMV, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvDMV, self).solve_optimization_problem()


class gscvDMVY(fnc_DMVY, InterfaceGSCV):
    def __init__(self):
        super(gscvDMVY, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvDMVY, self).solve_optimization_problem()


class gscvEWMV(fnc_EWMV, InterfaceGSCV):
    def __init__(self):
        super(gscvEWMV, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvEWMV, self).solve_optimization_problem()

class gscvCUSTOM(fnc_CUSTOM, InterfaceGSCV):
    def __init__(self):
        super(gscvCUSTOM, self).__init__()

    def solve_optimization_problem(self):
        return super(gscvCUSTOM, self).solve_optimization_problem()
