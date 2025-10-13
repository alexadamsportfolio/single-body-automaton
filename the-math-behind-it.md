## Introduction

Traditionally, the cellular automaton known as Langton's Ant consists of two structures: an underlying discrete grid of boolean values - our "field" - and an evolving position on that grid - our "body", more colloquially known as the "ant".
The rules are as follows: Given any iteration, the ant will find itself on either a black or white grid cell. If black, the ant will turn itself $90\degree$ counterclockwise; if white, $90\degree$ clockwise.
Then, the ant will step forth onto the grid cell adjacent to its origin cell in the direction determined by its rotation, and the original cell will have its boolean value toggled - white becomes black, and black white.

When I first learned about Langton's Ant as a high school junior one of the first things that I wanted to do was formulate an analogy on a 2-dimensional Euclidean plane with continuous, rather than boolean, values at each point. 
Seeing as the position of the body can be conceptualized by concatenating rotating step-arrows, it can be easily represented in terms of complex exponentials:

$$x_{n+1}=x_n+e^{i(\frac{\pi}{2}-\pi\phi_{n}(x_n)+\theta_n)} \\quad [\\mathrm{I}]$$

Where $x_n$ is the position of the body at iteration $n$, $\phi_{n}(x_n)$ is the the value of the underlying scalar field at point $x_n$, and $\theta_n$ is whatever the angle accumulated by the last iteration was.
Note that if $\phi_{n}(x_n)=0$ the exponential rotates by $\frac{\pi}{2}$ radians counterclockwise, and the same amount clockwise if $\phi_{n}(x_n)=1$, preserving the actions of white and black on the original Langton's Ant as those of 1 and 0 respectively.

## Part 1: The Body

Now recall that I said that $\theta_n$ is whatever the angle accumulated by the last iteration was. This means that

$$\theta_n=\frac{\pi}{2}-\pi\phi_{n-1}(x_{n-1})+\theta_{n-1} \\quad [\\mathrm{I}]$$

And assuming that $\theta_{0}=0$, we can collapse the recursion to obtain the closed form expression for $\theta_n$

$$\theta_n=\frac{\pi n}{2}-\pi\sum\limits_{j = 0}^{n-1} {\phi_{j}(x_j)} \\quad [\\mathrm{II}]$$

And an analogous formulation of equation [Introduction, I] like so

$$x_{n+1}=e^{\frac{i \pi (n+1)}{2}}\sum\limits_{j = 0}^{n} {e^{i\pi\sum\limits_{k = 0}^{j} {\phi_{k}(x_k)}}} \\quad [\\mathrm{III}]$$

Though space has been treated as continuous so far, we have still been treating the time parameter $n$ as discrete. However, we can design an analogy for continuous time by converting our summations into integrals

$$x_{\mu}=\int_{0}^{\mu} {e^{i(\frac{\pi \mu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)}} d\nu \\quad [\\mathrm{IV}]$$

Where $\mu$ is our new and continuous time parameter.

## Part 2: The Field

So far we have been sweeping the underlying scalar field $\phi: \mathbb{R}^2 \to [0,1]$ under the rug for the sake of simplicity; however, we should probably define it at some point. Particularly, we want it to satisfy the following 3 properties for each iteration:

1. $(\delta(a,x_n)=0) \land (\phi_{n}(a)=1) \implies (\phi_{n+1}(a)=0)$
2. $(\delta(a,x_n)=0) \land (\phi_{n}(a)=0) \implies (\phi_{n+1}(a)=1)$
3. $\phi_{n+1}(a) \sim \phi_{n}(a)$ as $\delta(a,x_n) \to \infty$

The first two conditions ensure that the values 0 and 1 are "toggled" on the positions from which the body moves, as is the case for the original Langton's Ant. The second condition ensures that for points sufficiently far away from the body, the perturbation in the scalar field is negligible.

There is probably a massive class of functions that satisfy the conditions for our scalar field, but the one I have been using in fish.py is the one that satisfies the recursive formula

$$\phi_{n+1}(a)=\phi_{n}(a)-\frac{\phi_{n}(a)+\phi_{n}(x_n)-1}{1+(a-x_n)(a-x_n)*} \\quad [\\mathrm{I}]$$

Recalling that $(a-x_n)(a-x_n)*$ is the magnitude of the difference between the complex numbers $a$ and $x_n$.

I have not yet found a closed-form expression for this definition of $\phi$, but I have noticed that the terms can be rearranged as 

$$\frac{\phi_{n+1}(a)-\phi_{n}(a)}{(n+1)-(n)}=\frac{\Delta \phi_n(a)}{\Delta n}=-\frac{\phi_{n}(a)+\phi_{n}(x_n)-1}{1+(a-x_n)(a-x_n)*} \\quad [\\mathrm{II}]$$

And, by converting the discrete change $\Delta$ to an infinitesimal change $d$, we get

$$\frac{d \phi_\mu(a)}{d \mu}=-\frac{\phi_{\mu}(a)+\phi_{\mu}(x_\mu)-1}{1+(a-x_\mu)(a-x_\mu)*} \\quad [\\mathrm{III}]$$

## Part 3: The Curvature

Since the output of fish.py strongly resembles an astrophysical orbit, has become a major goal of mine to identify a (pseudo-)Riemannian manifold on which the trajectory of the automaton body is a geodesic.
Luckily, we can derive the Riemann curvature tensor of such a manifold from its Christoffel connection coefficients: 

$$R^\rho_{\sigma \mu \nu}=\partial_\mu \Gamma^\rho_{\nu \sigma}-\partial_\nu \Gamma^\rho_{\mu \sigma}+\Gamma^\rho_{\mu \lambda} \Gamma^\lambda_{\nu \sigma}+\Gamma^\rho_{\nu \lambda} \Gamma^\lambda_{\mu \sigma}  \\quad [\mathrm{I}]$$

And the Christoffel coefficients can be realized from the geodesic equation for universal Newtonian time $\mu$, as in Newton-Cartan theory (since the field defined in [Part II, I] transforms instantaneously, violating relativistic causality):

$$\frac{\partial^2 x^k}{\partial \mu^2}=-\Gamma^k_{ij} \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu} \\quad [\mathrm{II}]$$

In other words, if the derivatives of $x^i$ and $x^j$ are non-degenerate,

$$\Gamma^k_{ij}=-\frac{\frac{\partial^2 x^k}{\partial \mu^2}}{ \frac{\partial x^i}{\partial \mu} \frac{\partial x^j}{\partial \mu}} 
\\quad [\mathrm{III}]$$

Conveniently for us, we know the three $x^k$ positions for the body from [Part I, IV]:

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

The nature of these differential equations, in conjunction with the harmonic phenomena implied by the field-automaton/life.py project, suggests to me that Laplace and/or Fourier transforms may prove useful. Furthermore, for sufficiently small values of $\mu$ we may approximate $sin(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho)$ as $\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho$, and $cos(\frac{\pi \mu}{2}-\pi\int_{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho)$ as $1$. These are very intriguing horizons, and I am excited to explore them when I get the opportunity. Granted, I must confess that the usage of a two-dimensional spatial projection of astrophysical phenomena typically observed in three spatial dimensions likely has been a source of error thus far.

I would like to close off this section with an image of my original computations for the Christoffel symbols:

![cce19838-521d-4d71-8878-677bb2189d9e 1280x1280](https://github.com/user-attachments/assets/ff64e161-35d7-4c7b-bd36-cd84a9856dd6)

## Closing Remarks

Progress has been slow, largely due to having little time between my numerous academic, extracurricular, vocational, and social obligations; I hope that I will have more opportunities to pursue my research after I graduate from high school. With regards to the single-body-automaton/fish.py project, I am interested in applying the tools of harmonic analysis to decompose the body's trajectory (since complex exponentials have been so ubiquitous thus far), as well as formulating alternative scalar fields whose transformations do not occur instantaneously across the entire space, but which experience some form of causal retardation - that is, locality. 

Though our equations have been nice and rigorous, it would be nice to visualize what sort of phenomena arise from them; this is why I created the fish.py program. And sure enough, fish.py reveals an orbit of varying precession and eccentricity very reminiscent of an orbital trajectory on the Kerr metric induced by a rotating black hole, suggesting a connection (no pun intended) to (pseudo-)Riemannian geometry; this isn’t too far-fetched, since the mutual interaction between the body and the scalar field determining its trajectory is greatly analogous to the correspondence between the stress-energy tensor and spacetime curvature. 

Here is the output of the automaton:

<img width="608" height="548" alt="Screenshot 2025-09-21 9 16 29 AM" src="https://github.com/user-attachments/assets/ca00dd51-83a8-4f47-80bb-218c359e6ab1" />

And the trajectory of an orbit around a rotating Kerr black hole (source: https://en.wikipedia.org/wiki/File:Orbit_around_a_rotating_Kerr_black_hole.gif):

![Orbit_around_a_rotating_Kerr_black_hole](https://github.com/user-attachments/assets/09add75c-1fcc-4bab-8b93-a5269362e5d2)

Thus, automata theory may provide an illuminating perspective on physics concerning curved fields such as general relativity, Berry curvature, and quantum gravity.
