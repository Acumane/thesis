import numpy as num
import matplotlib.pyplot as plot

samples = num.random.uniform(0, 10, 1000)

def calcErr(guess, samples):
    return num.mean(num.abs(guess - samples))

guesses = num.linspace(0, 10, 100)
errors = [calcErr(guess, samples) for guess in guesses]

strats = num.arange(11)
strat_errs = [calcErr(guess, samples) for guess in strats]

plot.figure(figsize=(12, 4))

plot.fill_between(guesses, errors, alpha=0.2, color="blue")
plot.scatter(guesses, errors, color='blue', s=10, alpha=0.5, label="Marginal payoff")

optimal_err = strat_errs[5]
plot.plot(5, optimal_err, "ro", markersize=10, label="Optimal strategy")
plot.axvline(x=5, color="g", linestyle="--", alpha=0.3, label="Mean")

plot.title("Optimal Guess Strategy over Uniform Distribution [0, 10]. 1,000 Trials ea.")
plot.xlabel("$S_n$ (n always guessed)")
plot.ylabel("Avg. abs. Error (ε)")
plot.grid(True, alpha=0.3)
plot.legend()

plot.annotate(f"ε ≈ {optimal_err:.1f}", 
            xy=(5, optimal_err),
            xytext=(5, optimal_err+0.5),
            color="red",
            fontsize=14,
            arrowprops=dict(facecolor="red", edgecolor="none", shrink=0.2))

plot.xlim(0, 10)
plot.ylim(bottom=0)

plot.savefig(".embed/uniform.png", bbox_inches="tight")
plot.close()