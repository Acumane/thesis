## Doomsday argument

Imagine you have two urns. Each contains a number of balls which are labeled sequentially. One urn contains ten balls (labeled 1-10), and the other contains a hundred (labeled 1-100). You don't know which urn is which, but you *are* allowed to reach in to one and randomly pick a ball. Imagine, too, that no amount of rummaging will tell you about the number of balls.

You inspect your chosen ball and find it's labeled #7. So, which urn did you choose? The one with ten or one hundred balls? Well, probably you drew from the 10-ball urn, right? After all, there was a 1-in-10 chance of getting that 7 from that urn, versus a 1-in-100 chance from the 100-ball urn. 

Formally, let $H_{10}$ and $H_{100}$ be our hypotheses for drawing from either urn, respectively, and let evidence $E$ be that we drew ball #7

Bayes' theorem states: $P(H_{10}|E) = \dfrac{P(E|H_{10}) \times P(H_{10})}{P(E)}$

Let's solve each part:
$P(H_{10}) = P(H_{100}) = 0.5$. Before inspecting our ball, we're equally likely to have picked from either urn.

$P(E|H_{10})$ = Probability of drawing ball #7 if in 10-ball urn = $\frac{1}{10}$

$P(E|H_{100})$ = Probability of drawing ball #7 if in 100-ball urn = $\frac{1}{100}$

$P(E) = P(E|H_{10}) \times P(H_{10}) + P(E|H_{100}) \times P(H_{100})$
   = $(\frac{1}{10} \times 0.5) + (\frac{1}{100} \times 0.5)$
   = $0.05 + 0.005$
   = $0.055$

So $P(H_{10}|E) = \dfrac{\frac{1}{10} \times 0.5}{0.055} = \dfrac{0.05}{0.055} \approx0.909$, or about 91%

Once we drew ball #7, we can believe with 91% certainty that we drew from the smaller, 10-ball urn. This happens to be consistent with our intuitions. 

Let's go again. Imagine there are two possible futures for humanity: in one, we colonize the Milky Way and persist for billions of years across countless star systems, ultimately giving rise to some million trillion trillion lives—$10^{22}$. In the other scenario, humanity never leaves the Earth. Our descendants, counted, amount to no more than the total number of people who have already lived—around 120 billion ($10^{11}$). We'll call these the doom-late and doom-soon scenarios respectively.

Like picking a ball, imagine that you could've been anyone along the interval that contains all past, future, and present members of humanity. These are the two urns: the doom-late urn contains $10^{22}$ lives and doom-soon contains $10^{11}$. Think of yourself as the numbered ball pulled from one of these, and the number imprinted on you is your birth rank (not birth date, which does away with population growth rates). For you, this is something like 120 billion. Now, which is more likely: that your birth rank happens to be somewhere around the midpoint our species, or that you belong to the first 0.0000001% of humans who will ever live? Our reasoning from the toy example also seems to favor the doom-soon scenario. And we've already picked our ball; we are the observation.

This is the doomsday argument. The observation of our existence suggests we're already a good fraction of the way to our expiration date. Some population growth models place "doomsday" farther away, but all more or less give us only a few centuries.

If you're at all suspect that we seem to have done humanity in with a bit of writing, you're in good company. Countless refutations have been made that cast ample doubt on this kind of reasoning, or at least its premises. Before we entertain them, let's attack the approach in a novel way. Whereas past detractors have argued that the doomsday "time bomb" is more likely a dud, my analysis will also reveal our countdown display is a faulty one.
