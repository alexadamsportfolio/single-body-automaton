# Necessary imports
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import math


# Ant class
class ant:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir


    @property
    def point(self):
        return [self.x, self.y]


# Define Euclidean metric
def distance(pointA, pointB, step):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) / step


# Update function
def update(frameNum, img, grid, N, step, weight, ant):
    newGrid = grid.copy()
   
    # Rotate ant
    ant.dir += (math.pi / 2) - (grid[int(round(ant.x)), int(round(ant.y))] * math.pi)

    # Change tile colors
    for i in range(N * step):
        for j in range(N * step):
            newGrid[i, j] = grid[i, j] - (grid[i, j] + grid[int(round(ant.x)), int(round(ant.y))] - 1) / (distance(ant.point, [i, j], step) ** weight + 1)
   
    # Move ant
    ant.x += step * math.cos(ant.dir)
    ant.y += step * math.sin(ant.dir)


    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


# main() function
def main():


    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # Parse arguments
    parser = argparse.ArgumentParser(description="Runs continuous Langton's Ant simulation.")


    # Add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--step-size', dest='stepSize', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--weight', dest='weight', required=False)
    args = parser.parse_args()
   
    # Set grid size
    N = 30
    if args.N:
        N = int(args.N)
       
    # Set step size
    stepSize = 1
    if args.stepSize:
        stepSize = int(args.stepSize)


    # Set distance weight
    weight = 1
    if args.weight:
        weight = float(args.weight)
       
    # Set animation update interval
    updateInterval = 1000
    if args.interval:
        updateInterval = int(args.interval)


    # Declare grid
    grid = np.full((N * stepSize, N * stepSize), 0.0, dtype=float)


    # Declare ants
    insect = ant(int(N * stepSize / 2), int(N * stepSize / 2), random.uniform(-math.pi / 2, math.pi / 2))


    # Set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', vmin=0, vmax=1, cmap='viridis')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, stepSize, weight, insect, ),
                                frames = 10,
                                interval=updateInterval,
                                save_count=50)


    # # of frames?
    # Set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])


    # Show plot
    plt.show()


# Call main
if __name__ == '__main__':
    main()
