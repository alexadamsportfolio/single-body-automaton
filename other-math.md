Though the-math-behind-it.md delineates the mathematics most necessary to the behavior of this project, it would be a shame for a STEM portfolio not to have some mention of my less successful findings - after all, the end is the smallest, and arguably the most trivial, stage in mathematics.
This document showcases my incomplete, if not incorrect, attempts on the single-body-automaton project; but they are no less interesting.

First and foremost, it was a major goal of mine to identify a pseudo-Riemannian manifold on which the trajectory of the automaton was a geodesic.
Luckily, we can derive the Riemann curvature tensor of such a manifold from its Christoffel connection coefficients: 

$$R^\rho_{\sigma \mu \nu}=\partial_\mu \Gamma^\rho_{\nu \sigma}-\partial_\nu \Gamma^\rho_{\mu \sigma}+\Gamma^\rho_{\mu \lambda} \Gamma^\lambda_{\nu \sigma}+\Gamma^\rho_{\nu \lambda} \Gamma^\lambda_{\mu \sigma}$$

And the Christoffel coefficients can be realized from the geodesic equation for universal Newtonian time $\mu$, as in Newton-Cartan theory:

$$\frac{\partial^2 x^k}{\partial \mu^2}=-\Gamma^k_{ij} \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}$$

In other words, if the derivatives of $x^i$ and $x^j$ are non-degenerate,

$$\Gamma^k_{ij}=-\frac{\frac{\partial^2 x^k}{\partial \mu^2}}{ \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}}$$

Conveniently for us, we know our three $x^k$ dimensions from the-math-behind-it.md:

$$x^0 = \mu$$
$$x^1 = $$
$$x^2 = $$
