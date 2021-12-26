<p align="center">
    <img width=40% src="https://github.com/faprieto96/pyInvestment/blob/master/docs/images/pipoh_logo.png?raw=true">
</p>

<!-- buttons -->
<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/python-v3-brightgreen.svg"
            alt="python"></a> &nbsp;
    <a href="https://pypi.org/project/PyPortfolioOpt/">
        <img src="https://img.shields.io/badge/pypi-v1.5.1-brightgreen.svg"
            alt="pypi"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg"
            alt="MIT license"></a> &nbsp;
    <a href="https://github.com/robertmartin8/PyPortfolioOpt/actions">
        <img src="https://github.com/robertmartin8/PyPortfolioOpt/workflows/pytest/badge.svg?event=push"
            alt="build"></a> &nbsp;
    <a href="https://pepy.tech/project/pyportfolioopt">
        <img src="https://pepy.tech/badge/pyportfolioopt"
            alt="downloads"></a> &nbsp;
    <a href="https://mybinder.org/v2/gh/robertmartin8/pyportfolioopt/master/?filepath=cookbook">
      <img src="https://mybinder.org/badge_logo.svg"
            alt="binder"></a> &nbsp;
</p>

<!-- content -->

## Introduction

Pipoh is a library that implements several diversification techniques base on mean-variance framework. 
In addition, it includes a novel purely data-driven methods for determining the optimal value of the hyper-parameters associated with each investment strategy like **Bayesian Optimization** or **Random Grid Search**. 

- [Diversification techniques for portfolio optimization:](https://github.com/faprieto96/pyInvestment/blob/master/docs/mv_formulation.md) 11 diversification and mean-variance strategies. 
- [Hyper-parameters description:](https://github.com/faprieto96/pyInvestment) Data-driven method for determining the optimal value of the hyper-parameter associated with each eppoch. 
- [Datasets description:](https://github.com/faprieto96/pyInvestment) 10 datasets focused on different markets. 
- [Performance evaluation metrics:](https://github.com/faprieto96/pyInvestment/blob/master/docs/performance_evaluation_metrics.md) Includes 4 metrics such as Mean Return, Sharpe Ratio, ... 

Pipoh is **extensive** and easily **extensible**, and it can be used to formulate your own strategies and use all capabilities of the library like hyper-parameters selection and evaluation metrics.

Pipoh has been conceived for different types of end-profiles.
- Investors and serious investment practitioners.
- Students that want to take contact with mean-variance strategies.
- Researchers that are looking for to desing, evaluate and test new strategies.

Head over to the **[documentation on ReadTheDocs](https://pyinvestment.readthedocs.io/en/latest/)** to get an in-depth look at the project.

<center>
<img src="https://github.com/faprieto96/pyInvestment/blob/master/docs/images/pipoh_architecture.png?raw=true" style="width:100%;"/>
</center>

## Table of contents

-   [Table of contents](#table-of-contents)
-   [Getting started](#getting-started)
    -   [For development](#for-development)
-   [A quick example](#a-quick-example)
-   [An overview of classical portfolio optimization methods](#an-overview-of-classical-portfolio-optimization-methods)
-   [Features](#features)
    -   [Expected returns](#expected-returns)
    -   [Risk models (covariance)](#risk-models-covariance)
    -   [Objective functions](#objective-functions)
    -   [Adding constraints or different objectives](#adding-constraints-or-different-objectives)
    -   [Black-Litterman allocation](#black-litterman-allocation)
    -   [Other optimizers](#other-optimizers)
-   [Advantages over existing implementations](#advantages-over-existing-implementations)
-   [Project principles and design decisions](#project-principles-and-design-decisions)
-   [Testing](#testing)
-   [Citing PyPortfolioOpt](#citing-pyportfolioopt)
-   [Contributing](#contributing)
-   [Getting in touch](#getting-in-touch)

## Getting started

If you would like to play with PyPortfolioOpt interactively in your browser, you may launch Binder [here](https://mybinder.org/v2/gh/robertmartin8/pyportfolioopt/master). It takes a
while to set up, but it lets you try out the cookbook recipes without having to deal with all of the requirements.

_Note: macOS users will need to install [Command Line Tools](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)._

_Note: if you are on windows, you first need to installl C++. ([download](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16), [install instructions](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view))_

This project is available on PyPI, meaning that you can just:

```bash
pip install pipoh
```

For more information, please read [this guide](https://docker-curriculum.com/#introduction).

### For development

If you would like to make major changes to integrate this with your proprietary system, 
it probably makes sense to clone this repository and to just use the source code.

```bash
git clone https://github.com/faprieto96/pipoh
```


## Quick examples

### First example: The user runs the Equally Weighted strategy that does not requires an optimization of the parameters.

```python
import pipoh

# Equally weighted strategy with dataset of emerging_markets
pipoh(strategy='EW', input_data='emerging_markets')
```

This outputs the following weights:

```txt
{'MR': -0.052464162446658, 
'SR': -0.008629148194608617, 
'CR': -0.001272997846970887, 
'Turnover': 0.11224602119519797}
```

### Second case: User optimizes the hyper-parameters with the Bayesian optimization.

```python
pipoh(strategy='WLBC', 
      optimization='Bayesian', 
      input_data='emerging_markets', 
      params={'lamb': ('cont', [0.5, 1]), 'lower_bound': ('cont', [0.8, 1])})
```

```txt
Evaluation 	 Proposed point 	  Current eval. 	 Best eval.
init   	 [0.62894893 0.90305801]. 	  -96.13552128609001 	 -96.13552128609001
init   	 [0.56036721 0.97370589]. 	  -96.13552128609001 	 -96.13552128609001
init   	 [0.54432336 0.8144007 ]. 	  -96.13552128609001 	 -96.13552128609001
1      	 [1. 1.]. 	  -96.13552128609001 	 -96.13552128609001

{'MR': -0.052464162446658, 'SR': -0.008629148194608617, 'CR': -0.001272997846970887, 'Turnover': 0.11224602119519797}
```


### Third case: User defines the strategy function

```python
def dominancia_estocastica(self):
    lambdaValue = self.lambda_value
    # lambdaValue = 0.886
    upperBoundValue = self.lower_bound
    return lambdaValue+upperBoundValue

params_defined = {'f': dominancia_estocastica, 'hp': {'lambda_value': ('cont', [0, 1]), 'lower_bound': ('cont', [0.1, 0.2])}, 'validation_windows':12}

ejemplo3 = pipoh(strategy='CustomStrategy', optimization='Bayesian', input_data='emerging_markets', params=params_defined)
```

```txt
Evaluation 	 Proposed point 	  Current eval. 	 Best eval.
init   	 [0.70285662 0.10066641]. 	  10.537387371579229 	 10.537387371579229
init   	 [0.68027651 0.17786081]. 	  10.537387371579229 	 10.537387371579229
init   	 [0.04832844 0.17557546]. 	  10.537387371579229 	 10.537387371579229
1      	 [0.36779647 0.1       ]. 	  10.537387371579229 	 10.537387371579229

{'MR': -0.052464162446658, 'SR': -0.008629148194608617, 'CR': -0.001272997846970887, 'Turnover': 0.11224602119519797}
```

_Disclaimer: nothing about this project constitues investment advice, and the author bears no responsibiltiy for your subsequent investment decisions. Please refer to the [license](https://github.com/robertmartin8/PyPortfolioOpt/blob/master/LICENSE.txt) for more information._


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


## Citing Pipoh

Pipoh methodology has been approved and peer reviewed by several scientist in the world. Articles related to this work can be checked in the following links.

1. [Mean Squared Variance Portfolio: A Mixed-Integer Linear Programming Formulation](http://dx.doi.org/10.3390/math9030223)
2. [Publication link](https://joss.theoj.org/papers/10.21105/joss.03066)

If you use Pipoh for published work, please cite above works. Citations string:

```text
1. Fernández-Navarro, F., Martínez-Nieto, L., Carbonero-Ruz, M., & Montero-Romero, T. (2021). Mean squared variance portfolio: A mixed-integer linear programming formulation. Mathematics, 9(3), http://dx.doi.org/10.3390/math9030223
```

## Contributing

Contributions are _most welcome_. Have a look at the [Contribution Guide](https://github.com/robertmartin8/PyPortfolioOpt/blob/master/CONTRIBUTING.md) for more.

I'd like to thank all of the people who have contributed to pipoh since its release in 2021.
Special shout-outs to:

-   Francisco de Asís Fernández Navarro
-   David Becerra Alonso

## Getting in touch

If you are having a problem with pipoh, please raise a GitHub issue.