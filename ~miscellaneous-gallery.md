Though the-math-behind-it.md delineates the mathematics most necessary to the behavior of this project, it would be a shame for a STEM portfolio not to have some mention of my less successful findings - after all, the end is the smallest, and arguably the most trivial, stage in mathematics.
This is a gallery of the surviving minority of my incomplete, if not incorrect, attempts on the single-body-automaton project; but they are no less interesting.

Below is an archaic formulation of the automaton, in terms of vectors over the polar coordinates. This would prove to be a very inconvenient formulation, demanding a change in origin for every iteration, and the complex exponentials formalized in the-math-behind-it.md would replace them.

![5b574418-6d34-460e-a3c7-d94b6db1b955 1280x1280](https://github.com/user-attachments/assets/708c0f27-0872-40cd-ae97-df01ce6d40d7)

Moving on, the math classes offered at my school are so basic that I will often pursue my own problems instead of taking notes for them (my grade is 98% in the class and the teacher doesn't mind). Here is some work I did for the automaton instead of taking notes for statistics: 

![ab2a703a-2a24-41d1-90d2-94d067e5aeab 1280x1280](https://github.com/user-attachments/assets/28874261-d0df-47e4-882c-ae659bbb235b)

The scribbled-out math at the top of the page is a failed formulation of the scalar field underlying single-body-automaton/fish.py. The upper middle of the page is a faulty closed-form expression for the position of the body; I made the rookie mistake of claiming that $\int e^{f(x)} dx = \frac{e^{f(x)}}{\int f(x) dx}$, but it's actually $\int e^{f(x)} dx = \frac{e^{f(x)}}{f{\prime}(x)}$, and this is only true when $f(x)$ is linear. The lower middle of the page is a differential equation relating the field to its time derivative, and its derivation was actually valid enough to make it into [Part 2, III] of the-math-behind-it.md. Finally, the bottom is an incomplete attempt to derive a closed-form expression for the scalar field.

Probably the greatest congregation of equations that validly describe the automaton is the whiteboard on my wall, where we can see that all of the equations - with the exception of [VI] - made it into the-math-behind-it.md:

![a097a8f9-6490-4cb6-af64-ebc6a5820de0 1280x1280](https://github.com/user-attachments/assets/0efc373f-acda-46b8-b140-bca2ba8a7c1e)

Equation [VI] is of particular interest to me, as it seeks to describe the automaton as a nonhomogeneous differential equation and thence apply a Laplace transform to unravel it, and as I have mentioned in the-math-behind-it.md, I have no doubt that there will be a breadth of interesting harmonic phenomena underlying it.

I would like to conclude this gallery with an image of me at the Texas State Capitol with fish.py and life.py, where I would present my programs to the 89th Texas Legislature for the CS4TX Code @ The Capitol Event.

![41db24d5-d21e-4b9a-b470-6f5384a2ce5c 1280x1280](https://github.com/user-attachments/assets/dc98e21c-02e7-496a-84ac-6c13bd829c53)
