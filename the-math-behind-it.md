$$ \textbf{Introduction} $$

Traditionally, the cellular automaton known as Langton's Ant consists of two structures: an underlying discrete grid of boolean values - our "field" - and an evolving position on that grid - our "body", more colloquially known as the "ant".
The rules are as follows: Given any iteration, the ant will find itself on either a black or white grid cell. If black, the ant will turn itself $90\degree$ counterclockwise; if white, $90\degree$ clockwise.
Then, the ant will step forth onto the grid cell adjacent to its origin cell in the direction determined by its rotation, and the original cell will have its boolean value toggled - white becomes black, and black white.

Now, what I wanted to do was formulate an analogy for Langton's Ant on a 2-dimensional Euclidean plane with continuous, rather than boolean, values at each point. 
Seeing as the position of the body can be conceptualized by concatenating rotating step-arrows, it can be easily represented in terms of complex exponentials:

$$x_{n+1}=x_n+e^{i(\frac{\pi}{2}-\pi\phi_{n}(x_n)+\theta_n)}  [\\mathrm{I}]$$

Where $x_n$ is the position of the body at iteration $n$, $\phi_{n}(x_n)$ is the the value of the underlying scalar field at point $x_n$, and $\theta_n$ is whatever the angle accumulated by the last iteration was.
Note that if $\phi_{n}(x_n)=0$ the exponential rotates by $\frac{pi}{2}$ radians counterclockwise, and the same amount clockwise if $\phi_{n}(x_n)=0$, preserving the actions of white and black on the original Langton's Ants as those of 1 and 0 respectively.

$$ \textbf{Part 1: The Body} $$

Now recall that I said that $\theta_n$ is whatever the angle accumulated by the last iteration was. This means that

$$\theta_n=\frac{\pi}{2}-\pi\phi_{n-1}(x_{n-1})+\theta_{n-1}  [\\mathrm{II}]$$

And assuming that $\theta_{0}=0$, we can collapse the recursion to obtain the closed form expression for $\theta_n$

$$\theta_n=\frac{\pi n}{2}-\pi\sum\limits_{j = 0}^{n-1} {\phi_{j}(x_j)}  [\\mathrm{III}]$$

And an analogous formulation of equation $[\\mathrm{I}]$ like so

$$x_{n+1}=\sum\limits_{j = 0}^{n} {e^{i(\frac{\pi (j+1)}{2}-\pi\sum\limits_{k = 0}^{j} {\phi_{k}(x_k)})}}  [\\mathrm{IV}]$$

Though space has been treated as continuous so far, we have still been treating the time parameter $n$ as discrete. However, we can design an analogy for continuous time by converting our summations into integrals

$$x_{\mu}=\int_{0}^{\mu} {e^{i(\frac{\pi \nu}{2}-\pi\int_{0}^{\nu} {\phi_{\rho}(x_\rho)} d\rho)}} d\nu  [\\mathrm{V}]$$

Where $\mu$ is our new and continuous time parameter.

$$ \textbf{Part 2: The Field} $$

So far we have been sweeping the underlying scalar field $\phi: \mathbb{R}^2 \to [0,1]$ under the rug for the sake of simplicity; however, we should probably define it at some point. Particularly, we want it to satisfy the following 3 properties for each iteration:

1. $(\delta(a,x_n)=0) \land (\phi_{n}(a)=1) \implies (\phi_{n+1}(a)=0)$
2. $(\delta(a,x_n)=0) \land (\phi_{n}(a)=0) \implies (\phi_{n+1}(a)=1)$
3. $\phi_{n+1}(a) \sim \phi_{n}(a)$ as $\delta(a,x_n) \to \infty$

The first two conditions ensure that the values 0 and 1 are "toggled" on the positions from which the body moves, as is the case for the original Langton's Ant. The second condition ensures that for points sufficiently far away from the body, the perturbation in the scalar field is negligible.

There is probably a massive class of functions that satisfy the conditions for our scalar fields, but the one I have been using in fish.py is the one that satisfies the recursive formula

$$\phi_{n+1}(a)=\phi_{n}(a)-\frac{\phi_{n}(a)+\phi_{n}(x_n)-1}{1+(a-x_n)(a-x_n)*}  [\\mathrm{I}]$$

Recalling that $(a-x_n)(a-x_n)*$ is the magnitude of the difference between the complex numbers $a$ and $x_n$.

I have not yet found a closed-form expression for this definition of $\phi$, but I have noticed that the terms can be rearranged as 

$$\frac{\phi_{n+1}(a)-\phi_{n}(a)}{(n+1)-(n)}=\frac{\Delta \phi_n(a)}{\Delta n}=-\frac{\phi_{n}(a)+\phi_{n}(x_n)-1}{1+(a-x_n)(a-x_n)*}  [\\mathrm{II}]$$

And, by converting the discrete change $\Delta$ to an infinitesimal change $d$, we get

$$\frac{d \phi_\mu(a)}{d \mu}=-\frac{\phi_{\mu}(a)+\phi_{\mu}(x_\mu)-1}{1+(a-x_\mu)(a-x_\mu)*}  [\\mathrm{III}]$$

$$ \textbf{Closing Remarks} $$

Progress has been slow, largely due to having little time between my numerous academic, extracurricular, vocational, and social obligations; I hope that I will have more opportunities to pursue my research after I graduate from high school. With regards to the single-body-automaton/fish.py project, I am interested in applying the tools of harmonic analysis to decompose the body's trajectory (since complex exponentials have been so ubiquitous thus far), as well as formulating alternative scalar fields whose transformations do not occur instantaneously across the entire space, but which experience some form of causal retardation - that is, locality. I am also curious about identifying a pseudo-Riemannian 2-manifold on which the trajectory of the body is a geodesic, for reasons that will be motivated in the next paragraph.

Though our equations have been nice and rigorous, it would be nice to visualize what sort of phenomena arise from them; this is why I created the fish.py program. And sure enough, fish.py reveals an orbit of gradual precession and shifting eccentricity, which is very reminiscent of the trajectory of Mercury under the Schwarzschild metric, suggesting a connection (no pun intended) to differential geometry; this isn’t too far-fetched, since the mutual interaction between the body and the scalar field determining its trajectory is greatly analogous to the correspondence between the stress-energy tensor and spacetime curvature. Thus, automata theory may provide an illuminating perspective on physics concerning curved fields such as general relativity, Berry curvature, and quantum gravity.
