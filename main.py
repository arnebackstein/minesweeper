# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()

font = pygame.font.SysFont('arial', 50)

width = 10
height = 10
scaling = 50
numOfMines = 15

screen = pygame.display.set_mode([width*scaling, height*scaling])
# Background
hintergrund= pygame.image.load("Bildschirmfoto 2021-10-01 um 13.37.40.png")
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



#for q in range (width):
    #for a in range (height):
        #if grid[q][a]== 0:
            #for v in range (-1,1):
                #for s in range(-1, 1):
                   # if v + q < 0 or v + q > width - 1 or s + a < 0 or s + a > height - 1:
                       # continue
                 #   if grid[q+v][a+s]== -1:
                      #  if s== 0 and v==0:
                     #       continue
                    #    grid[q][a] += 1
for q in range (width):
    for a in range (height):
        if grid[q][a]== -1:
            for v in range (-1,2):
                for s in range(-1, 2):
                    if v + q < 0 or v + q > width - 1 or s + a < 0 or s + a > height - 1:
                        continue
                    if grid[q+v][a+s]!= -1:
                        if s== 0 and v==0:
                            continue
                        grid[q+v][a+s] += 1





for row in grid:
    print(row)

screen.blit(hintergrund,(0, 0))

blue = (0,0,255)
#linien x-achse
for i in range(1,10):
    pygame.draw.line(screen, (0,0,0), [0+50*i,0], [0+50*i, 500] )
    pygame.draw.line(screen, (0, 0, 0), [0, 0 + 50 * i], [500, 0 + 50 * i])


def draw_number(number, x,y):
    text = font.render(str(number), True, (0, 0, 0))
    screen.blit(text, (x, y))
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos1 = pygame.mouse.get_pos()
            print(int(pos1[0] /scaling), int(pos1[1] / scaling))
            draw_number(1, 50,50)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()