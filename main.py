import pygame
import os
from game import Game

def main():
    pygame.init()
    font = pygame.font.SysFont('arial', 50)
    width, height, scaling, num_mines = 10, 10, 50, 15

    # Load backgrounds
    background_dir = "background_imgs"
    background_files = [f for f in os.listdir(background_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    background_paths = [os.path.join(background_dir, f) for f in background_files]

    screen = pygame.display.set_mode([width * scaling, height * scaling])
    game = Game(width, height, num_mines, scaling, background_paths)
    game.run(screen, font)

if __name__ == "__main__":
    main()