from concrete_factories.gscv_folder.gscv_interface import InterfaceGSCV


class gscvCustomStrategy(InterfaceGSCV):
    #En el init poner los parametros que quiera
    def __init__(self):
        pass

    def get_dimensions(self):
        return 'ok'

    def get_all_parameters(self):
        return "ok"

    def get_hyper_parameters(self):
        return "Hyper parameters selection done"

    def solve_optimization_problem(self):
        try:
            for x, y in self.values.items():
                if x != 'f' and x != 'hp':
                    exec('self.{}=y'.format(x, x))
        except:
            pass
        self.f(self)
        return 1

