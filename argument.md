
## Gott's Argument

Gott's "$\Delta t$ argument" is simply:
1. Given we're measuring *only* between times $t_{begin}$ and $t_{end}$
2. Barring anything special about $t_{now}$

Then "we expect $t_{now}$ to be located randomly in this interval." This is basically just the principle of mediocrity.


Since $t_{begin}$ and $t_{end}$ could be anything, we'll use $r = (t_{now} - t_{begin})/(t_{end} - t_{begin})$ to normalize our observation of $t_{now}$ to a value between 0 and 1. For such a value, Gott says "...there is a probability $P = 0.95$ that $0.025 < r < 0.975$".
Or, visually:

<center>

<img src="./.embed/gott-1.png" width="500px">

Possible world $w_1$

</center>

On closer inspection, Gott hasn't really discovered anything. Except for the trivial case that we are 100% sure $t_{now}$ belongs to this interval (which is guaranteed by premise 1), every other confidence interval $P < 1$ can be expressed an infinite amount of ways.
For example, we are just as confident that our $t_{now}$ won't belong to the middle 5%:

<center>
<img src="./.embed/gott-2.png" width="500px">

Possible world $w_2$

</center>


The problem is that, in spite of our high confidence in $w_1$, we believe equally ($P = 0.95$) in all worlds whose 5% disbelief fall within $w_1$'s 95%. The distribution is ultimately uniform, and $t_{now}$ could be from anywhere along it. The same confidence interval for $r$ (normalized $t_{now}$) in $w_1$ can be interpreted as a statement about $(t_{end} - t_{now})$—or in other words, the future.
Let $t_{past} = (t_{now} - t_{begin})$⠀and⠀$t_{future} = (t_{end} - t_{now})$,⠀so now⠀$r = \frac{t_{past}}{t_{past} + t_{future}}$. All we've done is started thinking about beginnings and ends as distances from *now* (plus, it's cleaner). 

<table width="100%"><tr>
<td>

For the lower bound (0.025):
$0.025 = \frac{t_{past}}{t_{past} + t_{future}}$, isolate:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀$t_{future} = 39t_{past}$

</td>
<td>

For the upper bound (0.975):
$0.975 = \frac{t_{past}}{t_{past} + t_{future}}$, isolate:
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀$t_{future} = \frac{1}{39}t_{past}$

</td>
</tr></table>

So for $w_1$'s confidence interval, $\frac{1}{39}t_{past} < t_{future} < 39t_{past}$. We'll need such estimates for the Doomsday argument.

---

Using Gott's logic, Bostrom suggests we assume:
 $t_{future} = (t_{end} - t_{now}) \approx t_{past} = (t_{now} - t_{begin})$

Or in other words, we *pretend* that the series will continue for roughly as long as it's already lasted. Ignoring any boring wins caught by whatever tolerance we assign to the word "roughly" ($\pm$ 0.01%, 2.5%, etc.), we're almost always wrong and overshoot as often as we undershoot—50/50 odds. It's reasonable to question why being symmetrically wrong would be preferable to any other strategy. Bostrom doesn't appear to offer any stronger reasoning than an appeal to neutrality, and our concerns with Gott's original argument certainly give us no reason to prefer $w_2$.


## My argument

If we instead measure how wrong we are, it becomes very clear that picking the mean is the dominant strategy. If you always pick 5, you'll never be more than 5 off. Whereas fringe strategies like 0 and 10 will be 10 off half as often, but 9 off almost as often, 8 not far behind, etc. Let's run a simulation for strategies $S_0$ to $S_{10}$ and see if this checks out:
<center><img src="./.embed/uniform.png" width="500px"></center>

Looks correct. Estimated error appears to be quadratic. $\varepsilon$ converges on half its strategy's distance from either end, and worst-case $\varepsilon$ is always half of world size. Worth keeping in mind for the math ahead.

Let's attempt to mathematize—experiment and intuition gets us only so far. Imagine our world $w$ is somewhere along a line from 0 to $W$, your guess $G$ divides this line into two segments. The expected error of these two segments are integrals over $G-w$ and $w-G$, respectively. To find our total expected error function $E_W(G)$, we add them:
$$
E_W(G) = \frac{1}{W} \left( \int_{0}^{G} (G - w) dw + \int_{G}^{W} (w - G) dw \right) = \frac{1}{W} \left( \frac{G^2}{2} + \frac{(W - G)^2}{2} \right)
$$
$$
E_W(G) = \frac{G^2 - W G + \frac{1}{2} W^2}{W}
$$
The numerator is our parabola observed in the simulation above. You can think of the denominator as normalizing over world size, giving us the average expected error per unit length. A precondition is that $G\leq W$, which is satisfied on account of having set $W$ ourselves, ostensibly because we believe larger worlds could not exist.
But let's consider it since it'll be important in a moment. If $G > W$, then $E_W(G) = G - \frac{W}{2}$. It's linear because we've lost the uncertainty of "walking" in the wrong direction; we're just subtracting the mean of the distribution.

Notice our toy example was given a discrete, unambiguous beginning and end [0,10]. This would be the equivalent of knowing our world size, which is not known to anyone but clairvoyants. To begin predicting optimal strategies for the Doomsday argument, we must account for this.

### Assumptions
According to our own rationale, we must reason as if we are a random sample from the interval. A fine statement on its own, but I'm straining credulity if I ask you to reason before you've observed you can reason. No person reading has yet to make an observation. So we must determine how one, from behind a Rawlsian veil of ignorance—a magical place where one can reason without belonging to the human reference class—would bet. With knowledge about the universe (expansion of space or some cosmic filter), we might conclude that $W_2$ is finite. And so long as you believe there is some world to speak of, you must entertain the idea that you could be "Adam" (i.e. before observing, your world was size 0). Obviously, no negative population can exist, so our lower bound must be 0. Fixing this term doesn't change much mathematically, so both $W_1$ and $W_2$  will remain free until later.

Lastly, we will assume our true world size $W$ is uniformly distributed between $W_1$ and $W_2$; that is, we believe all possible worlds belonging to this interval are equally possible. Although we might consider some worlds more likely than others, we think so given auxillary evidence and should treat this as a prior in need of updating. Therefore, the overall expected error $E(G)$ is:

$$
E(G) = \frac{1}{W_2 - W_1} \left( \int_{W_1}^{W_2} E_W(G) \, dW \right)
$$

But this integral is discontinous! As seen in our toy example, our expected error follows a different function when our $G>W$. Sure, we'll still never bet above our upper bound $W_2$, but all $G$s above $W_1$ risk this too.


So we evaluate them seperately:⠀$E(G) = \dfrac{I_1 + I_2}{W_2 - W_1}$,⠀where...

1. $I_1$ is for worlds where $G \leq W$ (Integrate over $W$ from $W_1$ to $G$):

$$
I_1 = \int_{W_1}^{G} \left( G - \frac{W}{2} \right) dW = \left[ G W - \frac{W^2}{4} \right]_{W_1}^{G}
$$

2. $I_2$ is for worlds where $G > W$ (Integrate over $W$ from $G$ to $W_2$)
$$
I_2 = \int_{G}^{W_2} \left( \frac{G^2 - W G + \frac{1}{2} W^2}{W} \right) dW = G^2 \ln\left( \frac{W_2}{G} \right) - G(W_2 - G) + \frac{1}{4} (W_2^2 - G^2)
$$


After performing the integrations and simplifying, we arrive at:

$$
E(G) = \frac{1}{W_2 - W_1} \left[ \frac{3}{2} G^2 - G(W_1 + W_2) + \frac{1}{4} (W_1^2 + W_2^2) + G^2 \ln\left( \frac{W_2}{G} \right) \right]
$$

To find the optimal (lowest) error guess $G^\star$, we'll need to find when $E(G)$'s derivative = 0:

$$
\frac{dE}{dG} = \frac{1}{W_2 - W_1} \left[ 2G (1 + \ln\left( \frac{W_2}{G} \right)) - (W_1 + W_2) \right] = 0
$$

$$
G + G\ln\left( \frac{W_2}{G} \right) = \frac{W_1 + W_2}{2}
$$

The $G$ inside the logarithm makes this impossible to solve algebraically, but we can converge on the solution with an algorithm. The following simulation imlements this algorithm and also tries every strategy $S_0$ to $S_{100}$ on an increasing number of possible worlds between $W_1$ = 0 and $W_2$ = 100:

<center>
<img src="./.embed/doomsday-0.gif" width="900px">
</center>

The simulated optimal strategy approaches our theoretical value. Good news!


WIP, to come:
- determine credence in $G^\star$
- how to deal with unbounded $W_2$ (infinite world)
