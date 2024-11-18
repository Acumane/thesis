In the fewest words, Anthropic reasoning involves:

1. Noticing an ever-present [selection effect](https://en.wikipedia.org/wiki/Selection_bias)
2. Reasoning according to simple statistical principle

---

### 1.
Observation selection effects arise from the precondition that an observer must exist to collect and analyze data.

Consider life on Earth: one might conclude that intelligent life emerging here suggests it's common on planets such as ours. But we necessarily find ourselves on a planet where intelligence evolved, regardless of its cosmic rarity. So the observation selection effect tells us we are exceptional, but not *how* exceptional, and certainly no more than necessary. Even if we could telepathically conduct a blind census of every alien civilization to evolve, they would all report evolving on life-bearing worlds—telling us nothing about how often this kind of thing happens naturally.

Another selection effect might be more elucidating:
If a lock, which typically takes $t=$ 100 hours to pick, must be picked within 1 hour, the only successful attempts will be those rare, lucky ones. The probability of success within time $T$ decays exponentially with $t/T$. But among *successful* attempts, the distribution of completion times becomes nearly identical for all very difficult locks ($t \gg T$). In fact, when examining successful attempts, we cannot distinguish between locks of different difficulties once they're sufficiently harder than our cutoff of 1 hour. A lock that takes 1 hour on average might pass for one that took 100; 100 will look identical to one that's often 1 million hours (again, if we only observe attempts that succeeded within an hour).


We may be able to use our [survivorship bias](https://en.wikipedia.org/wiki/Survivorship_bias) to say something about how "hard" it was for intelligent life to evolve on Earth. If the lock, so to speak, must be picked by the dusk of our main sequence star (10Byrs) and evolution is very hard ( $\gg$ 10Byrs), then we should expect to see it in its death throes. Instead, we find ourselves with 5.4Byrs to spare. 

### 2.
We should expect our position as observers to be typical rather than exceptional—that is, we should reason as if we're randomly sampled from the set of all observers. Where does this come from?

Consider Gott's "$\Delta t$ argument": if we observe a phenomenon at time $t_{now}$, and assume nothing special about our temporal position, we should expect $t_{now}$ to be randomly located between $t_{begin}$ and $t_{end}$. Although we know little of the distribution from which we sample phenomena, we'll be right more often than not if we guess $t_{now}$ is the average—or in other words, $t_{future} \approx t_{past}$. If this feels unintuitive, see how I discover this visually in my [simulation of the Doomsday problem](doomsday.md).

For a model like Gott's to work, one must be convinced that samples are being drawn from the phenomenon's expected duration (the "no-outsider" requirement). Consider two ways of observing a show on Broadway. Inside the theater, seeing a show tells you nothing about its run length—you're guaranteed to see it. But standing on Broadway, the very fact that you're seeing a show rather than an empty theater says something; longer-running shows are more likely to be encountered randomly. Sampling with outsiders, observing a phenomenon exists *at all* is evidence toward its longevity.

The Self-sampling assumption (SSA) accounts for this problem: reason as if you're randomly selected from all observers in your reference class. More precise formulations can (and will) be made, but this is the idea*

*Neither "$\Delta t$" nor SSA assert you are random in the objective sense of there being a physical randomization mechanism responsible for bringing you into the world. Further, both are optimal strategies—not laws. We only update our priors instead of making definitive claims.
