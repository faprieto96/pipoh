# Diversification techniques for portfolio optimization

Mathematically speaking, the MV portfolio framework is a quadratic optimization problem where an efficient frontier is composed of all combination assets that obtain the maximum return with the minimum risk. Return and risk are estimated through past price series, using the expected value and variance, respectively.

The baseline theory assumes that the means and covariances of the underlying asset returns are known.


Markowitz’s optimization problem determines, for a portfolio consisting of 𝑁 assets $(𝑛 = 1,…,𝑁)$, the optimal weights of the portfolio’s value invested in each asset, $𝑤_1,…,𝑤_𝑁 (\sum_{𝑛=1} ^{N} 𝑤_𝑛 = 1)$, using as the inputs of the problem the expected returns $(\mu_𝑛)$, risks $(\sigma_𝑛)$ and covariances between the assets (𝜎𝑛𝑚) (Kalayci et al., 2019; Markowitz, 1952). For ease of reference, the portfolio mean and variance are mathematically expressed as follows:

$$(\sum_{n=1} ^{N} w_N + \mu_n)$$
$$(\sum_{n,m=1} ^{N} w_N  \mu_n \sigma_{nm})$$ 


The two objectives associated with the theory can be addressed independently as two independent optimization problems. Mathematically, the global maximum return (GMR) portfolio is a convex optimization problem that can be formulated as follows:

$$(\max_{w_1,...,w_N} \sum_{n=1} ^{N} w_N\mu_{n})$$

s.t. 
$$\sum_{n=1} ^{N} w_N =1$$
$$(w_1,...,w_N \geq 0)$$

with the trivial solution of allocating all budget to the asset of maximum return. Unfortunately, this approach lacks diversification and traditionally performs poorly because past performance is not a guarantee of future performance.

Because of the above-mentioned information, it may be stated that the mean–variance (MV) portfolio theory is extensively employed by the community for constructing optimal portfolios.


**** !!!!!!! NO QUIERO PONER TODA LA FORMULACIÓN, POR LO QUE DEBERÍAMOS HACER UNA INTRO Y YA ENTRAR EN LA FORMULACIÓN DE LAS ESTRATEGIAS *****

The diversification techniques includes in the library are eleven. The complete list is:

### Equally weighted approaches
1. Equally weighted (EW) or 1/N portfolios.
2. Equally weighted risk contributions (EWRC).
3. Maximum diversification (MD).

### Controlling upper and lower bounds
4. Weighted upper bound constraints (WUBC).
5. Weighted lower bound constraints (WLBC).

### Cost function approaches
6. Diversified mean-variance strategy (DMV).
7. Diversified mean-variance strategy with yagger's entropy (DMVY).
8. Equally weighted minium variance (EWMV).

### Markowitz baseline formulation
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
