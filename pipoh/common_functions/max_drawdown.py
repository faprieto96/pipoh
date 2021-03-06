import numpy as np


def max_drawdown(STRATEGY_SELECTED):
    # Maximum drawdown is defined as the largest drop from a peak to a bottom
    # experienced in a certain time period.
    # OUTPUTS:
    # MDD...   Maximum drawdown expressed as a log return figure
    # MDDs...  Start of maximum drawdown period expressed as an
    #          index on vector aReturnVector
    # MDDe...  End of maximum drawdown period expressed as an
    #          index on vector aReturnVector
    # MDDr...  End of recovery period expressed as an index on vector
    #          aReturnVector

    n = max(STRATEGY_SELECTED.returns.shape)
    # calculate vector of cum returns
    cr = np.cumsum((np.asarray(STRATEGY_SELECTED.returns)).flatten(), axis=0)
    # calculate drawdown vector
    dd = []
    for i in range(0, n):
        if i == 0:
            dd.append(cr[i]- cr[i])
        if i>0:
            dd.append(max(cr[0:i]) - cr[i])
    dd = np.array(dd)

    # calculate maximum drawdown statistics
    MDD = max(dd)
    MDDe = np.where(dd == MDD)[0][0]
    MDDs = np.where(abs(cr[MDDe] + MDD - cr) < 0.000001)[0][0]
    if len(np.where(cr[MDDe:] >= cr[MDDs])[0])==0:
        MDDr = MDDe -1
    if len(np.where(cr[MDDe:] >= cr[MDDs])[0])>0:
        MDDr = MDDe + min(np.where(cr[MDDe:] >= cr[MDDs])) - 1

    ratios = {}
    ratios['MDD'] = MDD
    ratios['MDDs'] = MDDs
    ratios['MDDe'] = MDDe
    ratios['MDDr'] = MDDr

    return ratios
