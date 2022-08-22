# Welcome to Pipoh


<!-- buttons -->
<p align="left">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg"
            alt="python"></a> &nbsp;
    <a href="https://pypi.org/project/Pipoh/">
        <img src="https://img.shields.io/badge/pypi-v0.0.1-brightgreen.svg"
            alt="pypi"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg"
            alt="MIT license"></a>
</p>

Pipoh is a library that implements several diversification techniques base on mean-variance framework.  The well-known MV portfolio framework is based under the assumption that a rational investor wants to maximize their returns and minimize the risk associated with the portfolio.

In addition, it includes novel purely data-driven methods for determining the optimal value of the hyper-parameters associated with each investment strategy like **Bayesian Optimization** or **Random Grid Search**. 

Main of the capabilities included in Pipoh are:
- [Diversification techniques for portfolio optimization:](03_mv_formulation_files/index_mv_formulation.md) 11 diversification and mean-variance strategies. 
- [Hyper-parameters description:](https://github.com/faprieto96/pyInvestment) Data-driven method for determining the optimal value of the hyper-parameter associated with each eppoch. 
- [Datasets description:](https://github.com/faprieto96/pyInvestment) 10 datasets focused on different markets. 
- [Performance evaluation metrics:](https://github.com/faprieto96/pyInvestment/blob/master/docs/performance_evaluation_metrics.md) Includes 6 performance metrics.

Pipoh is **extensive** and easily **extensible**, and it can be used to formulate your own strategies and use all capabilities of the library like hyper-parameters selection and evaluation metrics.

Pipoh has been conceived for different types of end-profiles.
- Investors and serious investment practitioners.
- Students that want to take contact with mean-variance strategies.
- Researchers that are looking for to desing, evaluate and test new strategies.

Head over to the **[documentation on ReadTheDocs](https://pipoh.readthedocs.io/en/latest/)** to get an in-depth look at the project.

<center>
<img src="https://github.com/faprieto96/pyInvestment/blob/master/docs/images/pipoh_architecture.png?raw=true" style="width:100%;"/>
</center>


## Getting started

This project is available on PyPI, meaning that you work with Pipoh just running the following command:

```bash
pip install pipoh
```

### For development

If you would like to make major changes to integrate this with your proprietary system, 
it probably makes sense to clone this repository and to just use the source code.

```bash
git clone https://github.com/faprieto96/pipoh
```



## Quick examples

### First example: Running an Equally Weighted Strategy without optimization.

An user wants to run the *Equally Weighted strategy* with the dataset of Emerging Markets. This strategy does not requires an optimization of its parameters.

```python
import pipoh

# Equally weighted strategy with dataset of emerging_markets
pipoh(strategy='EW', input_data='emerging_markets')
```

By default, Pipoh library will return the performance metrics:

```txt
{'Mean Return': 0.2538425925925927, 
'Share Ratio': 0.04657430634672944, 
'Calmar Ratio': 0.007121075161565159, 
'Colog Ratio': 0.008545319323776479, 
'MiniMax ratio': 2.9118428040361115, 
'Turnover': 0.0}
```

### Second case: Running an Weighted Lower Bound Constraint Strategy with an optimization of its hyper-parameters.

User optimizes the hyper-parameters with the Bayesian optimization.

```python
pipoh(strategy='WLBC', 
      optimization='Bayesian', 
      input_data='emerging_markets', 
      params={'lamb': ('cont', [0.5, 1]), 'lower_bound': ('cont', [0.8, 1])})
```

```txt
# Performance evaluation metrics
Evaluation       Proposed point           Current eval.          Best eval.
init     [0.52384733 0.09224026].         43.88902890653751      43.88902890653751
init     [0.62067801 0.08772509].         43.88902890653751      43.88902890653751
init     [0.63399604 0.00299079].         43.88902890653751      43.88902890653751
1        [0.56996903 0.03656443].         43.88902890653751      43.88902890653751
{'Mean Return': 0.12893810329370484, 'Share Ratio': 0.022784737436991786, 
'Calmar Ratio': 0.003331248264446595, 'Colog Ratio': 0.004026306008939107, 
'MiniMax ratio': 1.0000000000000002, 'Turnover': 0.0398582808840518}
```


### Third case: An user defines a customized strategy function.

```python
def dominancia_estocastica(self):
    lambdaValue = self.lambda_value
    upperBoundValue = self.lower_bound
    return lambdaValue+upperBoundValue

params_defined = {'f': dominancia_estocastica, 'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}

pipoh(strategy='CustomStrategy', optimization='Bayesian', input_data='emerging_markets', params=params_defined)
```

```txt
Evaluation 	 Proposed point 	  Current eval. 	 Best eval.
init   	 [0.16350618 0.16670019]. 	  7.530597410893871 	 7.530597410893871
init   	 [0.53640884 0.13407134]. 	  7.530597410893871 	 7.530597410893871
init   	 [0.70007243 0.18761661]. 	  7.530597410893871 	 7.530597410893871
1      	 [0.41013578 0.2       ]. 	  7.530597410893871 	 7.530597410893871
{'Mean Return': 6.076666666666665, 'Share Ratio': 0.1327915894897509, 
'Calmar Ratio': 0.03640902736169362, 'Colog Ratio': 0.0029018551134198343, 
'MiniMax ratio': 1.1969796454366382, 'Turnover': 0.0}
```

_Disclaimer: nothing about this project constitues investment advice, and the author bears no responsibiltiy for your subsequent investment decisions. Please refer to the [license](https://github.com/faprieto96/pipoh/blob/master/license.txt) for more information._


## Project principles and design decisions

-   It should be easy to swap out individual components of the optimization process
    with the user's proprietary improvements.
-   Usability is everything: it is better to be self-explanatory than consistent.
-   There is no point in portfolio optimization unless it can be practically
    applied to real asset prices.
-   Everything that has been implemented should be tested.
-   Inline documentation is good: dedicated (separate) documentation is better.
    The two are not mutually exclusive.
-   Formatting should never get in the way of coding: because of this,
    I have deferred **all** formatting decisions to [Black](https://github.com/ambv/black).


## Citing Pipoh and related work.

Pipoh methodology has been approved and peer reviewed by several scientist in the world. Articles related to this work can be checked in the following links.

1. [Mean Squared Variance Portfolio: A Mixed-Integer Linear Programming Formulation](http://dx.doi.org/10.3390/math9030223)

If you use Pipoh for published work, please cite above works. Citations string:

```text
1. Fernández-Navarro, F., Martínez-Nieto, L., Carbonero-Ruz, M., & Montero-Romero, T. (2021). Mean squared variance portfolio: A mixed-integer linear programming formulation. Mathematics, 9(3), http://dx.doi.org/10.3390/math9030223
```

## Contributing

Contributions are _most welcome_. 

I'd like to thank all of the people who have contributed to pipoh since its release in 2021.
Special shout-outs to:

-   Francisco de Asís Fernández Navarro
-   David Becerra Alonso

## Getting in touch

If you are having a problem with pipoh, please raise a GitHub issue.