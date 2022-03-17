# Installation

## Quick Start with Pip:
Under Pip commanda, Pipoh is full avaibable:

    pip install pipoh

How to use Pipoh:

```python
import pipoh

# Equally weighted strategy with dataset of emerging_markets
pipoh(strategy='EW', input_data='emerging_markets')
```

This will generate the following output:

```txt
{'Mean Return': 0.2538425925925927, 
'Share Ratio': 0.04657430634672944, 
'Calmar Ratio': 0.007121075161565159, 
'Colog Ratio': 0.008545319323776479, 
'MiniMax ratio': 2.9118428040361115, 
'Turnover': 0.0}
```

## Quick Start with the project-template:
This package serves as a skeleton package aiding at developing compatible scikit-learn contribution.
To create your package, you need to clone the project-template repository:

    git clone https://github.com/faprieto96/pipoh
