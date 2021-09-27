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



for q in range (width):
    for a in range (height):
        if grid[q][a]== 0:
            for v in range (-1,1):
                for s in range(-1, 1):
                    if v + q < 0 or v + q > width - 1 or s + a < 0 or s + a > height - 1:
                        continue
                    if grid[q+v][a+s]== -1:
                        if s== 0 and v==0:
                            continue
                        grid[q][a] += 1




for row in grid:
    print(row)



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