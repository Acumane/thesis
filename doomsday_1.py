import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P
from scipy.optimize import minimize_scalar

# Configuration
W1, W2, trials = 0, 100, 500

def calcErr(g, w, trials):
    """Calculate error for guess g and world of size w"""
    samples = np.random.uniform(0, w, trials)
    return np.mean(np.abs(g - samples))

def simulate(worlds):
    """Run simulation for given worlds"""
    guesses = np.linspace(0, W2, W2)  # Fixed range for all scenarios
    errors = np.zeros(len(guesses))
    
    for i, g in enumerate(guesses):
        w_errors = []
        for _ in range(trials):
            w = np.random.choice(worlds)
            error = calcErr(g, w, 1)
            w_errors.append(error)
        errors[i] = np.mean(w_errors)

    # Fit cubic polynomial
    coeffs = P.polyfit(guesses, errors, deg=3)
    best_fit = P.polyval(guesses, coeffs)

    # optimal strategy from best fit:
    i = np.argmin(best_fit)
    min_g = guesses[i]
    min_err = best_fit[i]
    
    return guesses, errors, best_fit, min_g, min_err

def modelE(g, W1, W2):
    """Model E(g) over all possible worlds."""
    if W1 == W2:
        return np.abs(g - W1)
    
    E = np.zeros_like(g)
    
    # For g <= W1
    mask1 = g <= W1
    g1 = g[mask1]
    if len(g1) > 0:
        E[mask1] = ((W1 + W2) / 2 - g1) / (W2 - W1)
    
    # For W1 < g <= W2
    mask2 = (g > W1) & (g <= W2)
    g2 = g[mask2]
    if len(g2) > 0:
        term1 = (1.5 * g2**2 - g2 * (W1 + W2) + 0.25 * (W1**2 + W2**2))
        term2 = g2**2 * np.log(W2 / g2)
        E[mask2] = (term1 + term2) / (W2 - W1)
    
    # For g > W2
    mask3 = g > W2
    g3 = g[mask3]
    if len(g3) > 0:
        E[mask3] = (g3 - (W1 + W2) / 2)
    
    return np.nan_to_num(E, nan=0.0, posinf=1e6, neginf=-1e6)

def minimizeE(W1, W2):
    """Solve for g_star and its min_err"""
    if W1 == W2:
        return W1, 0
    
    result = minimize_scalar(
        lambda x: modelE(np.array([x]), W1, W2)[0],
        bounds=(W1, W2),
        method="bounded"
    )
    return result.x, result.fun

# Define scenarios with increasing resolution
scenarios = [
    ("2 worlds\n(dw = 100)", np.linspace(W1, W2, 2).astype(int)),
    ("4 worlds\n(dw ≈ 33)", np.linspace(W1, W2, 4).astype(int)),
    ("8 worlds\n(dw ≈ 14.3)", np.linspace(W1, W2, 8).astype(int)),
    ("All worlds\n(dw = 1)", np.linspace(W1, W2, 101).astype(int))
]

# Create figure with more space for labels
fig = plt.figure(figsize=(20, 11))
gs = fig.add_gridspec(2, 2, hspace=0.2, wspace=0.15)
axs = gs.subplots()
axs = axs.ravel()

plt.suptitle("World Size Guess Strategies as lim(dw→1)", y=0.95, fontsize=18)

for idx, (title, worlds) in enumerate(scenarios):
    ax = axs[idx]
    
    # Run simulation:
    guesses, errors, best_fit, min_g, min_err = simulate(worlds)

    ax.plot(guesses, errors, "b.", alpha=0.25, markersize=4)
    ax.fill_between(guesses, errors, alpha=0.1, color="blue")
    ax.plot(guesses, best_fit, "k:", linewidth=2, label="Cubic fit")
    ax.plot(min_g, min_err, "kx", markersize=10, label="Cubic minimum")

    # Use model:
    guesses = np.linspace(0.1, W2, W2)  # Start from 0.1 instead of 0
    errors = modelE(guesses, W1, W2)
    g_star, min_err = minimizeE(W1, W2)

    ax.plot(guesses, errors, "r-", alpha=0.8, linewidth=2, label="E(g) curve")
    ax.plot(g_star, min_err, "ro", markersize=10, label=f"g* @ {g_star:.2f}")

    ax.annotate(f"ε ≈ {min_err:.2f}", # g_star annotation
        xy=(g_star, min_err),
        arrowprops=dict(facecolor="red", edgecolor="none", shrink=0.2, width=2),
        xytext=(g_star, min_err - 8),
        color="red", fontsize=12,
        ha="center")

    ax.set_xlim(0, W2)
    ax.set_ylim(0, 80)

    ax.set_xticks(worlds) # Ticks represent possible worlds
    ax.set_xticklabels(["0" if x == W1 else "100" if x == W2 else "" for x in worlds])
    ax.text(0.05, 0.95, title, transform=ax.transAxes, 
            fontsize=14,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.8),
            verticalalignment="top")
    
    ax.grid(True, alpha=0.3)

# Add legend inside the last subplot
axs[-1].legend(loc="lower right")

fig.supxlabel("Strategy (g)", y=0.04, fontsize=16)
fig.supylabel("Expected abs. error (ε)", x=0.08, fontsize=16)

plt.savefig(".embed/doomsday-1.png", dpi=300, bbox_inches="tight")
plt.close()