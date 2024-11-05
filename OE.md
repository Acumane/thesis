## Observation Equation

The conditional probability of hypothesis $h$ conditioned on evidence $e$ from the perspective of observer-moment $\alpha$ is:

$$P_\alpha(h|e) = \frac{1}{\gamma} \sum_{\sigma \in \Omega_h \cap \Omega_e} \frac{P_\alpha(w_\sigma)}{|\Omega_\sigma \cap \Omega(w_\sigma)|}$$

Where:
- $\sigma$ are "relevant" observer-moments: observer-moments for which hypothesis $h$ and evidence $e$ are both true
- $\Omega$ are reference classes; $w$ are (possible) worlds
- $\gamma$ is a normalization constant to ensure probabilities sum to 1:

$$
\gamma = \sum_{\sigma \in \Omega_e} \frac{P_\alpha(w_\sigma)}{|\Omega_\sigma \cap \Omega(w_\sigma)|}
$$

Or in other words, sum the following over all "relevant" observer-moments $\sigma$:
- (Normalization coeff $\dfrac{1}{\gamma}$) $\times$ (certainty that observer-moment $\alpha$ belongs to world $w_\sigma$) $\div$ (the number of relevant observer-moments belonging to world $w_\sigma$)


Notice the conventional reference class $\Omega_\alpha$ (observer-moments like $\alpha$) is missing. OE uses what I'm calling the "relevant" class ($\Omega_\sigma$) instead.
