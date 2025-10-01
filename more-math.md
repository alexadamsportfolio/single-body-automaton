Though the-math-behind-it.md delineates the mathematics most necessary to the behavior of this project, it would be a shame for a STEM portfolio not to have some mention of my less successful findings - after all, the end is the smallest, and arguably the most trivial, stage in mathematics.
This document showcases my incomplete, if not incorrect, attempts on the single-body-automaton project; but they are no less interesting.

## An Attempt to Derive the Curvature Tensor for the Automaton Space

It has been a major goal of mine to identify a pseudo-Riemannian manifold on which the trajectory of the automaton body is a geodesic.
Luckily, we can derive the Riemann curvature tensor of such a manifold from its Christoffel connection coefficients: 

$$R^\rho_{\sigma \mu \nu}=\partial_\mu \Gamma^\rho_{\nu \sigma}-\partial_\nu \Gamma^\rho_{\mu \sigma}+\Gamma^\rho_{\mu \lambda} \Gamma^\lambda_{\nu \sigma}+\Gamma^\rho_{\nu \lambda} \Gamma^\lambda_{\mu \sigma}  \\quad [\mathrm{I}]$$

And the Christoffel coefficients can be realized from the geodesic equation for universal Newtonian time $\mu$, as in Newton-Cartan theory:

$$\frac{\partial^2 x^k}{\partial \mu^2}=-\Gamma^k_{ij} \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}`\\quad [\mathrm{II}]$$

In other words, if the derivatives of $x^i$ and $x^j$ are non-degenerate,

$$\Gamma^k_{ij}=-\frac{\frac{\partial^2 x^k}{\partial \mu^2}}{ \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}} 
\\quad [\mathrm{III}]$$

Conveniently for us, we know the three $x^k$ positions for the body from the-math-behind-it.md [Part I, IV]:

$$x^0 = \mu  \\quad [\mathrm{IV.a}]$$
$$x^1 = Re(\int_{0}^{\mu} {e^{i(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)}} d\nu)=\int_{0}^{\mu} {cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu  \\quad [\mathrm{IV.b}]$$
$$x^2 = Im(\int_{0}^{\mu} {e^{i(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)}} d\nu) = \int_{0}^{\mu} {sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu  \\quad [\mathrm{IV.c}]$$

Seeing as $x^0$ is linear with respect to $\mu$ - as is to be expected from a universal Newtonian parameter - the Christoffel symbols of superscript $0$ would be trivial for all $i$ and $j$:

$$\Gamma^0_{ij}=0  \\quad [\mathrm{V}]$$

However, noting that

$$\frac{\partial x^1}{\partial \mu}=cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) - \frac{\pi}{2} \int_{0}^{\mu} {sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu  \\quad [\mathrm{VI.a}]$$
$$\frac{\partial x^2}{\partial \mu}=sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) + \frac{\pi}{2} \int_{0}^{\mu} {cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu  \\quad [\mathrm{VI.b}]$$
$$\frac{\partial^2 x^1}{\partial \mu^2}=-(\frac{\pi}{2}-\pi\phi_{\mu}(x_\mu))sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) - \frac{\pi}{2} \int_{0}^{\mu} {sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu - \frac{\pi^2}{4} \int_{0}^{\mu} {cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu  \\quad [\mathrm{VI.c}]$$
$$\frac{\partial^2 x^2}{\partial \mu^2}=(\frac{\pi}{2}-\pi\phi_{\mu}(x_\mu))cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) + \frac{\pi}{2} \int_{0}^{\mu} {cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu - \frac{\pi^2}{4} \int_{0}^{\mu} {sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)} d\nu \\quad [\mathrm{VI.d}]$$

The other Christoffel symbols, let alone the curvature tensor, become very unwieldly, so I will spare your eyes and omit them; just recall [III] if you really want to see them.

Though a clean, closed-form exact solution likely does not exist - which is not uncommon in non-Euclidean astrophysics - we can still take note of interesting properties to implicitly study the behavior of this system. For instance, we can plug the identities in [IV] into equations [VI] to obtain these interesting systems of differential equations:

$$\frac{\partial x^1}{\partial \mu}=cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) - \frac{\pi}{2} x^2  \\quad [\mathrm{VII.a}]$$
$$\frac{\partial x^2}{\partial \mu}=sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) + \frac{\pi}{2} x^1  \\quad [\mathrm{VII.b}]$$
$$\frac{\partial^2 x^1}{\partial \mu^2}=-(\frac{\pi}{2}-\pi\phi_{\mu}(x_\mu))sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) - \frac{\pi}{2} x^2 - \frac{\pi^2}{4} x^1  \\quad [\mathrm{VII.c}]$$
$$\frac{\partial^2 x^2}{\partial \mu^2}=(\frac{\pi}{2}-\pi\phi_{\mu}(x_\mu))cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho) + \frac{\pi}{2} x^1 - \frac{\pi^2}{4} x^2 \\quad [\mathrm{VII.d}]$$

The nature of these differential equations, in conjunction with the harmonic phenomena implied by the field-automaton/life.py project, suggests to me that Laplace and/or Fourier transforms may prove useful. Furthermore, for sufficiently small values of $\mu$ we may approximate $sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho)$ as $\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho$, and $cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho)$ as $1$. These are very intriguing horizons, and I am excited to explore them when I get the opportunity. I would like to close off this section with an image of my original computations for the Christoffel symbols:

<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/1fa72799-51d0-43ae-a3c3-496ae2fa72b8" />
