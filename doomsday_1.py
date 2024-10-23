import random
from numpy import histogram, trapz
import matplotlib.pyplot as plot
from matplotlib.animation import FuncAnimation as Anim

w1, w2, trials = 10, 100, 1_000_000

def doomsday(trials, getEnd):
    errors = []
    for _ in range(trials):
        beg, end = 1, getEnd()
        now = random.uniform(beg, end+1)  # [1, end]
        past = now - beg  # future estimate
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
    (lambda: random.choice([w1, w2]), "2 worlds (dw = 90)"),
    (lambda: random.choice(possibles(w1, w2, res=4)), "4 worlds (dw = 30)"),
    (lambda: random.choice(possibles(w1, w2, res=10)), "10 worlds (dw = 10)"),
    (lambda: random.choice(possibles(w1, w2, res=19)), "19 worlds (dw = 5)"),
    (lambda: random.randint(w1, w2+1), "91 worlds (dw = 1)")  # [10, 100]
]

fig, ax = plot.subplots(figsize=(10, 6))
plot.suptitle("Correct Guess Distribution as lim(dw→0)", fontsize=14)

def animate(frame):
    ax.clear()
    ax.set_xlim(-w2, w2)
    ax.set_ylim(0, 0.05)
    ax.set_xlabel("Error (actual - estimated)")
    ax.set_ylabel("Density")
    ax.yaxis.grid(True, linestyle="--", color="lightgray")
    
    getEnd, subtitle = steps[frame]
    errors = doomsday(trials, getEnd)
    density, bins = histogram(errors, bins=100, range=(-w2, w2), density=True)
    bins = (bins[:-1] + bins[1:]) / 2  # bin centers
    
    ax.plot(bins, density, color="blue")
    ax.fill_between(bins, density, color="lightblue", alpha=0.5)

    area = trapz(density, bins) # integrate
    ax.legend([f"Area: {area:.2f}"], loc="upper right")
    ax.set_title(subtitle)
    return ax

anim = Anim(fig, animate, frames=len(steps), interval=1000, repeat=True)
anim.save(".embed/doomsday-1.gif", writer="pillow", fps=1)
