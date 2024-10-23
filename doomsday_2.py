import random
from numpy import histogram, trapz
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation as Anim

w1, w2, trials = 10, 100, 500_000

def doomsday(trials, _worlds, method):
    errors = []
    for _ in range(trials):
        worlds = _worlds()
        if type(worlds) is list:
            weights = worlds if method == "SIA" else None
            end = random.choices(worlds, weights=weights, k=1)[0]
        else: end = worlds
            
        now = random.uniform(1, end+1)
        past = now - 1
        future = end - now
        errors.append(future - past)
        # Expect equidistance to past & future
    return errors

def possibles(w1, w2, res):
    if res < 2: return [w1]
    step = (w2 - w1) / (res - 1)
    return [int(w1 + i * step) for i in range(res)]

steps = [
    (lambda: w1, "1 world"),
    (lambda: [w1, w2], "2 worlds (dw = 90)"),
    (lambda: possibles(w1, w2, res=4), "4 worlds (dw = 30)"),
    (lambda: possibles(w1, w2, res=10), "10 worlds (dw = 10)"),
    (lambda: possibles(w1, w2, res=19), "19 worlds (dw = 5)"),
    (lambda: list(range(w1, w2+1)), "91 worlds (dw = 1)")
]

fig, (ax1, ax2) = plot.subplots(1, 2, figsize=(15, 6))
plot.suptitle("Correct Guess Distribution as lim(dw→0)", fontsize=14)

def animate(frame):
    ax1.clear(); ax2.clear()

    for ax in [ax1, ax2]:
        ax.set_xlim(-w2, w2)
        ax.set_ylim(0, 0.05)
        ax.set_xlabel("Error (actual - estimated)")

        ax.set_ylabel("Density")
        ax.yaxis.grid(True, linestyle="--", color="lightgray")
    
    worlds, subtitle = steps[frame]
    
    # SSA plot
    errors = doomsday(trials, worlds, "SSA")
    density, bins = histogram(errors, bins=100, range=(-w2, w2), density=True)
    bins = (bins[:-1] + bins[1:]) / 2
    area = trapz(density, bins)  # bin centers
    
    ax1.plot(bins, density, color="blue")
    ax1.fill_between(bins, density, color="lightblue", alpha=0.5)
    ax1.legend([f"Area: {area:.2f}"], loc="upper right")
    ax1.set_title(f"SSA: {subtitle}")
    
    # SIA plot
    errors = doomsday(trials, worlds, "SIA")
    density, bins = histogram(errors, bins=100, range=(-w2, w2), density=True)
    bins = (bins[:-1] + bins[1:]) / 2
    area = trapz(density, bins)

    ax2.plot(bins, density, color="red")
    ax2.fill_between(bins, density, color="lightpink", alpha=0.5)
    ax2.legend([f"Area: {area:.2f}"], loc="upper right")
    ax2.set_title(f"SIA: {subtitle}")
    
    return ax1, ax2

anim = Anim(fig, animate, frames=len(steps), interval=1000, repeat=True)
anim.save(".embed/doomsday-2.gif", writer="pillow", fps=1)
