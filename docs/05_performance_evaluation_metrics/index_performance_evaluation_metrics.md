# Performance evaluation metrics

The diversification techniques includes in the library are eleven. The complete list is:

### Mean return (MR)
1. Equally weighted (EW) or 1/N portfolios.
2. Equally weighted risk contributions (EWRC).
3. Maximum diversification (MD).

### Sharpe ratio (SR)
4. Weighted upper bound constraints (WUBC).
5. Weighted lower bound constraints (WLBC).

### Calmar ratio (CR)
6. Diversified mean-variance strategy (DMV).
7. Diversified mean-variance strategy with yagger's entropy (DMVY).
8. Equally weighted minium variance (EWMV).

### Stability Index (SI)
9. Global Maximum Return (GMR).
10. Global Minimum Variance (GMV).

# Formulation of above strategies.
### 1. Equally weighted (EW) or 1/N portfolios.



For full documentation visit [pyInvestment GitHub Repository](https://github.com/faprieto96/pyInvestment).

PyInvestment is a library that implements mean-variance optimization methods. This library includes:

- 11 diversification and mean-variance strategies. [MV formulation.](https://github.com/faprieto96/pyInvestment)
- Data-driven method for determining the optimal value of the hyper-parameter associated with each eppoch. [Hyper-parameters description.](https://github.com/faprieto96/pyInvestment)
- 10 datasets focused on different markets. [Datasets description.](https://github.com/faprieto96/pyInvestment)



## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
