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
hintergrund = pygame.image.load("background.jpg")
hintergrund = pygame.transform.scale(hintergrund, (1280, 720))
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



def reveal(x,y):
    draw_number(grid[x][y], x*scaling + 10,y*scaling)
    grid[x][y] = -2

def reveal_recurse(x,y):
    for x_offset in range(-1, 1, 1):
        for y_offset in range(-1, 1, 1):
            x_t = x+x_offset
            y_t = y+y_offset
            print(x_t,y_t)
            reveal(x_t,y_t)

            if(grid[x_t][y_t] == 0):
                reveal_recurse(x_t,y_t)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if(left):
                pos1 = pygame.mouse.get_pos()
                print(int(pos1[0] /scaling), int(pos1[1] / scaling))
                x, y = int(pos1[0] /scaling), int(pos1[1] / scaling)
                if(grid[x][y] == 0):
                    reveal_recurse(x,y)
                elif(grid[x][y] == -1):
                    running = False
                else:
                    reveal(x,y)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
