Though the-math-behind-it.md delineates the mathematics most necessary to the behavior of this project, it would be a shame for a STEM portfolio not to have some mention of my less successful findings - after all, the end is the smallest, and arguably the most trivial, stage in mathematics.
This document showcases my incomplete, if not incorrect, attempts on the single-body-automaton project; but they are no less interesting.

First and foremost, it was a major goal of mine to identify a pseudo-Riemannian manifold on which the trajectory of the automaton was a geodesic.
Luckily, we can derive the metric tensor of such a manifold from its Christoffel connection coefficients, and the Christoffel coefficients can be realized from the geodesic equation for universal Newtonian time $\mu$, as in Newton-Cartan theory:

$$\frac{\partial^2 x^k}{\partial \mu^2}=-\Gamma^k_{ij} \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}$$
