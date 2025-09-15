Assuming that all necessary modules have been installed, fish.py can be easily run with

```python3 fish.py```

However, there are 4 optional parameters that will influence the behavior of the automaton:

- Grid Size: An integer value that establishes the number of cells are in each dimension for the 2d grid. Default is 30.
- Step Size: An integer value that determines how many cells the body moves for each iteration. Default is 1.
- Weight: A float value $k$, such that each cell on the grid is weighted by a factor of $\frac{1}{1+\delta^k}$, where $\delta$ is the distance in the Euclidean metric between that cell and the position of the body. Default is 1.
- Update Interval: Specifies the interval between iterations in milliseconds. Default is 1000.

Below is an example of fish.py being run with configured parameters:

```python3 fish.py --grid-size 50 --step-size 2 --weight 2.5 --interval 700```

And below is an example output of the automaton:

<img width="1919" height="1006" alt="image22" src="https://github.com/user-attachments/assets/473c7612-700c-4cf2-bc3f-29d2c25d177a" />

There is also a ```--mov-file``` parameter that presumably saves the animation to a file, but I've never bothered to test it.
