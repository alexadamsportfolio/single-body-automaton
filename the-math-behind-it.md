Traditionally, the cellular automaton known as Langton's Ant consists of two structures: an underlying discrete grid of boolean values, and an evolving position on that grid known as our "ant".
The rules are as follows: Given any iteration, the ant will find itself on either a black or white grid cell. If black, the ant will turn itself $90\degree$ counterclockwise; if white, $90\degree$ clockwise.
Then, the ant will step forth onto the grid cell adjacent to its origin cell in the direction determined by its rotation, and the original cell will have its boolean value toggled - white becomes black, and black white.

Now, what I wanted to do was formulate an analogy for Langton's Ant on a 2-dimensional Euclidean plane with continuous, rather than boolean, values at each point. 
Seeing as the position of the body can be visualized by concatenating rotating step-arrows, it can be easily represented in terms of complex exponentials:

$$x_{n+1}=x_n+e^{\frac{\pi}{2}-\pi\phi_{n}(x_n)+\theta_n}  [\\mathrm{I}]$$

Where $x_n$ is the position of the body at iteration $n$, $\phi_{n}(x_n)$ is the the value of the underlying scalar field at point $x_n$, and $\theta_n$ is whatever the angle accumulated by the last iteration was.
Note that if $\phi_{n}(x_n)=0$ the exponential rotates by $\frac{pi}{2}$ radians counterclockwise, and the same amount clockwise if $\phi_{n}(x_n)=0$, preserving the actions of white and black on the original Langton's Ants as those of 1 and 0 respectively.

Now recall that I said that $\theta_n$ is whatever the angle accumulated by the last iteration was. This means that

$$\theta_n=\frac{\pi}{2}-\pi\phi_{n-1}(x_{n-1})+\theta_{n-1}  [\\mathrm{II}]$$

And assuming that $\theta_{0}=0$, then we obtain the closed form expression for $\theta_n$

$$\theta_n=\frac{\pi n}{2}-\sum\limits_{i = 0}^{n-1} {\phi_{i}(x_i)}  [\\mathrm{III}]$$

Which we can plug into equation $[\\mathrm{I}]$ like so

$$x_{n+1}=x_n+e^{\frac{\pi (n+1)}{2}-\sum\limits_{i = 0}^{n} {\phi_{i}(x_i)}}  [\\mathrm{IV}]$$

Though space has been treated as continuous so far, we have still been treating the time parameter $n$ as discrete. However, we can design an continuous analogy for time by noticing that

$$x_{n+1}-x_n=\frac{x_{n+1}-x_n}{(n+1)-(n)}=\frac{\Delta x_n}{\Delta n}=e^{\frac{\pi (n+1)}{2}-\sum\limits_{i = 0}^{n} {\phi_{i}(x_i)}}  [\\mathrm{V}]$$

And, by converting the $\Delta$ an infinitesimal change $d$ , and the summation in the exponential to an integral, we get

$$\frac{dx_\mu}{d\mu}=e^{\frac{\pi (\mu+1)}{2}-\int{0}^{\mu} {\phi_{\rho}(x_\rho)} d\rho}  [\\mathrm{VI}]$$

Or, by taking the antiderivative,

NOTE TO SELF: IS THERE AN EXPRESSION FOR $x_\mu$?

Where $\mu$ is our new and continuous time parameter.
