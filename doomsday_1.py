import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy.polynomial import polynomial as P
from scipy.optimize import minimize_scalar

# Configuration
W1, W2, trials = 0, 100, 500

def calcErr(G, W, trials):
    """Calculate error for guess G and world of size W"""
    samples = np.random.uniform(0, W, trials)
    return np.mean(np.abs(G - samples))

def simulate(worlds):
    """Run simulation for given worlds"""
    guesses = np.linspace(0, W2, W2)  # Fixed range for all scenarios
    errors = np.zeros(len(guesses))
    
    for i, G in enumerate(guesses):
        W_errors = []
        for _ in range(trials):
            W = np.random.choice(worlds)
            error = calcErr(G, W, 1)
            W_errors.append(error)
        errors[i] = np.mean(W_errors)

    # Fit cubic polynomial
    coeffs = P.polyfit(guesses, errors, deg=3)
    best_fit = P.polyval(guesses, coeffs)

    # optimal strategy from best fit:
    i = np.argmin(best_fit)
    min_G = guesses[i]
    min_err = best_fit[i]
    
    return guesses, errors, best_fit, min_G, min_err

def modelE(G, W1, W2):
    """Model E(G) over all possible worlds."""
    if W1 == W2:
        return np.abs(G - W1)
    
    E = np.zeros_like(G)
    
    # For G <= W1
    mask1 = G <= W1
    G1 = G[mask1]
    if len(G1) > 0:
        E[mask1] = ((W1 + W2) / 2 - G1) / (W2 - W1)
    
    # For W1 < G <= W2
    mask2 = (G > W1) & (G <= W2)
    G2 = G[mask2]
    if len(G2) > 0:
        term1 = (1.5 * G2**2 - G2 * (W1 + W2) + 0.25 * (W1**2 + W2**2))
        term2 = G2**2 * np.log(W2 / G2)
        E[mask2] = (term1 + term2) / (W2 - W1)
    
    # For G > W2
    mask3 = G > W2
    G3 = G[mask3]
    if len(G3) > 0:
        E[mask3] = (G3 - (W1 + W2) / 2)
    
    return np.nan_to_num(E, nan=0.0, posinf=1e6, neginf=-1e6)

def minimizeE(W1, W2):
    """Solve for G_star and its min_err"""
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
    ("2 worlds (dW = 100)", np.linspace(W1, W2, 2).astype(int)),
    ("4 worlds (dW ≈ 33)", np.linspace(W1, W2, 4).astype(int)),
    ("8 worlds (dW ≈ 14.3)", np.linspace(W1, W2, 8).astype(int)),
    ("16 worlds (dW ≈ 6.6)", np.linspace(W1, W2, 16).astype(int)),
    ("Continuous (dW = 1)", np.linspace(W1, W2, 101).astype(int))
]

# Set up the figure
fig, ax = plt.subplots(figsize=(12, 6))
plt.suptitle("World Size Guess Strategies as lim(dW→0)", fontsize=14)

def animate(frame):
    ax.clear()
    title, worlds = scenarios[frame]

    # Run simulation:
    guesses, errors, best_fit, min_G, min_err = simulate(worlds)

    ax.plot(guesses, errors, "b.", alpha=0.25, markersize=4)
    ax.fill_between(guesses, errors, alpha=0.1, color="blue")
    ax.plot(guesses, best_fit, "k:", linewidth=2, label="Cubic fit")
    ax.plot(min_G, min_err, "kx", markersize=10, label="Cubic minimum")

    # Use model:
    guesses = np.linspace(0.1, W2, W2)  # Start from 0.1 instead of 0
    errors = modelE(guesses, W1, W2)
    G_star, min_err = minimizeE(W1, W2)

    ax.plot(guesses, errors, "r-", alpha=0.8, linewidth=2, label="E(G) curve")
    ax.plot(G_star, min_err, "ro", markersize=10, label=f"G* @ {G_star:.2f}")

    ax.annotate(f"ε ≈ {min_err:.2f}", # G_star annotation
        xy=(G_star, min_err),
        arrowprops=dict(facecolor="red", edgecolor="none", shrink=0.2, width=2),
        xytext=(G_star, min_err - 8),
        color="red", fontsize=12,
        ha="center")

    ax.set_xlim(0, W2)
    ax.set_ylim(0, 80)

    ax.set_xticks(worlds) # Ticks represent possible worlds
    ax.set_xticklabels(["0" if x == W1 else "100" if x == W2 else "" for x in worlds])

    ax.set_title(title)
    ax.set_xlabel("Strategy ($G$)")
    ax.set_ylabel("Expected abs. error (ε)")
    ax.grid(True, alpha=0.3)
    ax.legend()

# Create animation
anim = FuncAnimation(fig, animate, frames=len(scenarios), interval=2000, repeat=True)

anim.save(".embed/doomsday-0.gif", writer="pillow", fps=0.5)
plt.close()
