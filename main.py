# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()

width = 30
height = 30
scaling = 20
numOfMines = 15

screen = pygame.display.set_mode([width*scaling, height*scaling])

running = True

# (x,y) -> -1 == bomb, else num of neighbors
grid = list()


for x in range(width):
    grid.append(list())
    for y in range(height):
        grid[-1].append(0)


for _ in range(numOfMines):
    x = int(random.uniform(0, width))
    y = int(random.uniform(0, height))

    grid[x][y] = -1

t=0

for q in range (width):
    for a in range (height):
        if grid[q][a]== 0:
            for v in range (-1,1):
                for s in range (-1, 1):
                    if grid[q+v][a+s]:
                        if s== 0 and v==0:
                            continue
                        t=t+1
                        print(t)


print(grid)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()