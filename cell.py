class Cell:
    """Represents a single cell on the Minesweeper board."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.neighbor_mines = 0
        self.revealed = False
        self.flagged = False

    def reveal(self):
        self.revealed = True