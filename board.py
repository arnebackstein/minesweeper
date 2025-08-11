from cell import Cell

class Board:
    """Handles the Minesweeper board logic."""

    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.mines_placed = False

    def reveal_all_mines(self):
        for x in range(self.width):
            for y in range(self.height):
                cell = self.grid[x][y]
                if cell.is_mine:
                    cell.revealed = True

    def place_mines(self, avoid_x=None, avoid_y=None):
        import random
        placed = 0
        while placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x == avoid_x and y == avoid_y):
                continue
            cell = self.grid[x][y]
            if not cell.is_mine:
                cell.is_mine = True
                placed += 1
        self.mines_placed = True
        self.count_neighbors()

    def count_neighbors(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y].is_mine:
                    continue
                count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.grid[nx][ny].is_mine:
                                count += 1
                self.grid[x][y].neighbor_mines = count

    def reveal_cell(self, x, y):
        if not self.mines_placed:
            self.place_mines(avoid_x=x, avoid_y=y)
        cell = self.grid[x][y]
        if cell.revealed:
            return
        cell.reveal()
        if cell.neighbor_mines == 0 and not cell.is_mine:
            self.reveal_neighbors(x, y)

    def reveal_neighbors(self, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbor = self.grid[nx][ny]
                    if not neighbor.revealed and not neighbor.is_mine:
                        self.reveal_cell(nx, ny)

    def draw_grid_lines(self, screen, scaling):
        import pygame
        for i in range(1, self.width):
            pygame.draw.line(screen, (0, 0, 0), [0 + scaling * i, 0], [0 + scaling * i, self.height * scaling])
        for i in range(1, self.height):
            pygame.draw.line(screen, (0, 0, 0), [0, 0 + scaling * i], [self.width * scaling, 0 + scaling * i])