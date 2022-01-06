# Fichero que contiene la agrupación de todas las estrategias.

from strategies.individual_strategies.class_ew import fnc_EW
from strategies.individual_strategies.class_ew import fnc_EW
from strategies.individual_strategies.class_gmr import fnc_GMR
from strategies.individual_strategies.class_gmv import fnc_GMV
from strategies.individual_strategies.class_custom import fnc_CUSTOM

# Se importan las funciones, dentro de la clase que ejecutará.
# Es el método común de importar todas las funciones a partir de un fichero común de python.
# Todo proviene de la carpeta pipoh > strategies. Por lo que la función se modificaría en todas las carpetas.


class non_parameteric_EW(fnc_EW):
    def __init__(self):
        super(non_parameteric_EW, self).__init__()

    def solve_optimization_problem(self):
        return super(non_parameteric_EW, self).solve_optimization_problem()


class non_parameteric_GMR(fnc_GMR):
    def __init__(self):
        super(non_parameteric_GMR, self).__init__()

    def solve_optimization_problem(self):
        return super(non_parameteric_GMR, self).solve_optimization_problem()


class non_parameteric_GMV(fnc_GMV):
    def __init__(self):
        super(non_parameteric_GMV, self).__init__()

    def solve_optimization_problem(self):
        return super(non_parameteric_GMV, self).solve_optimization_problem()


class non_parameteric_CUSTOM(fnc_CUSTOM):
    def __init__(self):
        super(non_parameteric_CUSTOM, self).__init__()

    def solve_optimization_problem(self):
        return super(non_parameteric_CUSTOM, self).solve_optimization_problem()
