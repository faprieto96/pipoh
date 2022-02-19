# Diversification techniques for portfolio optimization

Mathematically speaking, the MV portfolio framework is a quadratic optimization problem where an efficient frontier is composed of all combination assets that obtain the maximum return with the minimum risk. Return and risk are estimated through past price series, using the expected value and variance, respectively.

The baseline theory assumes that the means and covariances of the underlying asset returns are known.


Markowitz’s optimization problem determines, for a portfolio consisting of 𝑁 assets (𝑛 = 1,…,𝑁), the optimal weights of the portfolio’s value invested in each asset,

.. math:: 

:math:`E(R)` is a Nx1 vector of expected returns, where *N* is the number of assets.
`(\sum_{𝑛=1} ^{N}`
$$𝑤_1,…,𝑤_𝑁 (\sum_{𝑛=1} ^{N} 𝑤_𝑛 = 1)$$

.. math::

    \begin{equation*}
    \begin{aligned}
    & \underset{w}{\text{maximise}} & & w^T \mu \\
    & \text{subject to} & & n^T n \leq s^*  \\
    &&& B w - p + n = 0 \\
    &&& w^T \mathbf{1} = 1 \\
    &&& n \geq 0 \\
    &&& p \geq 0. \\
    \end{aligned}
    \end{equation*}

using as the inputs of the problem the expected returns (𝜇𝑛), risks (𝜎𝑛) and covariances between the assets (𝜎𝑛𝑚) (Kalayci et al., 2019; Markowitz, 1952). For ease of reference, the portfolio mean and variance are mathematically expressed as follows:

$$(\sum_{n=1} ^{N} w_N + \mu_n)$$
$$(\sum_{n,m=1} ^{N} w_N  \mu_n \sigma_{nm})$$


The two objectives associated with the theory can be addressed independently as two independent optimization problems. Mathematically, the global maximum return (GMR) portfolio is a convex optimization problem that can be formulated as follows:

$$(\max_{w_1,...,w_N} \sum_{n=1} ^{N} w_N\mu_{n})$$

s.t.
$$\sum_{n=1} ^{N} w_N =1$$
$$(w_1,...,w_N \geq 0)$$

with the trivial solution of allocating all budget to the asset of maximum return. Unfortunately, this approach lacks diversification and traditionally performs poorly because past performance is not a guarantee of future performance.

Because of the above-mentioned information, it may be stated that the mean–variance (MV) portfolio theory is extensively employed by the community for constructing optimal portfolios.

The diversification techniques included in the library are:

### [Equally weighted approaches](mv_formulation_ew_approaches.md)

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

