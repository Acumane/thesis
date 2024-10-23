from random import randint, choice
import matplotlib.pyplot as plot
from fractions import Fraction
import numpy as num


def decide(freq):
    return "tails" if randint(0, 100) < freq \
    else "heads"

# Read incubator.md
def incubator(n, freq):
    correct = {'A': 0, 'B': 0}
    total = {'A': 0, 'B': 0}

    for _ in range(n):
        coin = choice(["heads", "tails"])
        
        if coin == "tails": rooms = ["black"]
        else: rooms = ["black", "white"]
        
        for _ in rooms: # Stage A
            total['A'] += 1
            if decide(freq) == coin:
                correct['A'] += 1
        
        if "black" in rooms: # Stage B
            total['B'] += 1
            if decide(freq) == coin:
                correct['B'] += 1

    return { # % correct
        'A': (correct['A'] / total['A']) * 100,
        'B': (correct['B'] / total['B']) * 100
    }

n, strat = 10000, num.linspace(0, 100, 101)
print(f"Running {n * len(strat)} trials...")
results = {s: incubator(n, s) for s in strat}

correct_A = [results[s]['A'] for s in strat]
correct_B = [results[s]['B'] for s in strat]

bestFit = lambda x : num.poly1d(num.polyfit(strat, x, 1)) 
line_A, line_B = bestFit(correct_A), bestFit(correct_B) 

plot.figure(figsize=(12, 6))
plot.scatter(strat, correct_A, label="Stage A", alpha=0.5)
plot.scatter(strat, correct_B, label="Stage B", alpha=0.5)
plot.plot(strat, line_A(strat), "--", color="tab:blue")
plot.plot(strat, line_B(strat), "--", color="tab:orange")

plot.xlabel("Strategy: T guess freq. (%)")
plot.ylabel("Correct (%)")
plot.suptitle("Correct Guess Distribution", fontsize=16)
plot.title(f"n={n} trials / strategy")

plot.legend()
plot.grid(True)
plot.savefig(".embed/incubator.png")

print("\nOptimal Cr(T):")
# If we *always* bet tails, how often do we win?
c_A, c_B = line_A(100), line_B(100) # P(T) = Cr(T)
frac = lambda n : Fraction(n/100).limit_denominator(10)

print(f"  A) {c_A:.1f}% ≈ {frac(c_A)}")
print(f"  B) {c_B:.1f}% ≈ {frac(c_B)}")
print("\nFigure saved to \"incubator.png\"")
