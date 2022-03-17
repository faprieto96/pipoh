# Equally weighted approaches


1. Equally weighted (EW) or 1/N portfolios.
2. Equally weighted risk contributions (EWRC).
3. Maximum diversification (MD).


## 1. Equally weighted (EW) or 1/N portfolios.

Optimal portfolios tend to be excessively concentrated in a limited subset of the full set of assets.

Optimal mean–variance (MV) portfolios generally tend to be excessively concentrated in a limited subset of the full set of assets (portfolio concentration). A simple and naive way to solve this problem is to attribute the same weight to all the assets included in the portfolio. Equally weighted (EW) or $1/N$ portfolios are widely used in the literature.

The main advantages of the 1∕𝑁 naive approach are that it does not need to estimate the moments of asset returns or optimize a particular objective function with constraints.

The main drawback of the $1∕𝑁$ rule is that it leads to very limited diversification of risks if individual risks are significantly different.


## 2. Equally weighted risk contributions (EWRC).

Risk parity is an approach that overcomes the previously mentioned limitation of the 1∕𝑁 rule by focusing on the allocation of risk rather than on the allocation of capital. The best-known version of risk parity is the equally weighted risk contributions (EWRC) portfolio method. This method quantifies the (total) risk contribution of the 𝑛th asset, taking into account the partial derivative of the risk function with respect to the weight of the $n^{th}$ asset:

$$
w_n \times \partial_{w_n}
(\sum_{n,m=1} ^{N} w_n w_m \sigma_{nm})
=
w_n \times \frac{w_n \sigma_n ^2 + \sum_{n \neq m}} {\sum_{n,m=1} ^{N} w_n w_m \sigma_{nm}}
\varpropto w_n \times (\sum w)_n
$$


where $\sum$  $\epsilon$ $\Re^{N \times N}$ is the covariance matrix, $w = (w_1,...,w_N)$ $\epsilon$ $\Re^{N}$ the vector of weights and $(\sum_w)_n$ the $n^{th}$ row of the vector of the matrix obtained from the product of $\sum$ with $w$. Equal risk contribution then
means that $w_n \times (\sum_w)_n = w_m \times (\sum_w)_m$ for all $n,m$.

## 3. Maximum Diversification (MD).

It should be noted that the EWRC strategy is inspired by the maximum diversification (MD) technique, which maximizes the following diversification ratio.

$$
max_{w_1,...w_N}
\frac {\sum_{n=1}^N w_n \sigma_{nn}} {\sum_{n,m=1}^N w_n w_m \sigma n_m}
$$

$$
s.t.

\sum_{n=1}^N w_n = 1
$$

$$
w_1, ..., w_N \geq 0
$$