
import pandas as pd
import numpy as np
# Input parameters of the model are introduced.
# By default, some parameters are introduce to help the usability of the final user.
from abc import ABCMeta, abstractmethod, ABC
from common_functions.list_data_repository import ListDataRepository





class Data(ABC, ListDataRepository):
    def __init__(self, data_requested) -> None:
        self.data_requested = data_requested

    def import_data(self):
        try:
            return eval('np.matrix(pd.read_csv(ListDataRepository.{}, header=None))'.format(self.data_requested))
        except SyntaxError or NameError or FileNotFoundError:
            return np.matrix(pd.read_csv(self.data_requested, header=None))


