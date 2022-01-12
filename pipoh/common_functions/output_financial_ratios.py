import numpy as np
from abc import ABC, abstractmethod

#Listado actual de ratios impolementados
# 1. Mean_Return
# 2. Sharpe_Ratio
# 3. Calmar_Ratio
# 4. Colog_ratio
# 5. MiniMax_ratio
# 6. turnover

@abstractmethod
def output_financial_ratios(STRATEGY_SELECTED):
    ratios = STRATEGY_SELECTED.ratios
    returns = STRATEGY_SELECTED.returns
    weights = STRATEGY_SELECTED.weights

    # Save number of elements and number of assets

    #n = max(returns.shape)
    Mean_Return = returns.mean()
    Sharpe_Ratio = Mean_Return/np.std(returns)
    MiniMax_ratio = Mean_Return / (returns-weights.min(axis=1)).mean()
    Colog_ratio = Mean_Return / np.var(returns)

    Calmar_Ratio = Mean_Return/ratios['MDD']

    (Q, N) = weights.shape
    turnover = (1/(Q-1))*(1/N) * sum(sum(abs(weights[2:, :]-weights[1:-1, :])))

    output_financial_ratios={}
    output_financial_ratios['Mean Return'] = Mean_Return
    output_financial_ratios['Share Ratio'] = Sharpe_Ratio
    output_financial_ratios['Calmar Ratio'] = Calmar_Ratio
    output_financial_ratios['Colog Ratio'] = Colog_ratio
    output_financial_ratios['MiniMax ratio'] = MiniMax_ratio
    output_financial_ratios['Turnover'] = turnover

    return output_financial_ratios