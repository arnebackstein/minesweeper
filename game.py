import pygame
import time
import os

from board import Board
from leaderboard import load_leaderboard, save_leaderboard
from ui import draw_menu, draw_background_selection, draw_leaderboard, draw_name_entry

class Game:
    def __init__(self, width, height, num_mines, scaling, background_paths):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.scaling = scaling
        self.background_paths = background_paths
        self.state = "menu"
        self.background_index = 0
        self.background = pygame.image.load(self.background_paths[self.background_index])
        self.background = pygame.transform.scale(self.background, (1280, 720))
        self.board = Board(width, height, num_mines)
        self.start_time = None
        self.win_time = None
        self.player_name = ""

    def check_win(self):
        for x in range(self.board.width):
            for y in range(self.board.height):
                cell = self.board.grid[x][y]
                if not cell.is_mine and not cell.revealed:
                    return False
        return True

    def restart(self):
        self.board = Board(self.width, self.height, self.num_mines)
        self.state = "playing"
        self.start_time = time.time()
        self.win_time = None
        self.player_name = ""

    def set_background(self, idx):
        self.background_index = idx
        self.background = pygame.image.load(self.background_paths[self.background_index])
        self.background = pygame.transform.scale(self.background, (1280, 720))

    def draw_flags(self, screen):
        for x in range(self.board.width):
            for y in range(self.board.height):
                cell = self.board.grid[x][y]
                if cell.flagged and not cell.revealed:
                    cx = cell.x * self.scaling + self.scaling // 2
                    cy = cell.y * self.scaling + self.scaling // 2
                    pygame.draw.polygon(
                        screen,
                        (255, 0, 0),
                        [
                            (cx - 10, cy + 15),
                            (cx - 10, cy - 15),
                            (cx + 15, cy)
                        ]
                    )

    def run(self, screen, font):
        menu_font = pygame.font.SysFont('arial', 40)
        small_font = pygame.font.SysFont('arial', 30)
        button_rect = pygame.Rect(self.width * self.scaling // 2 - 75, self.height * self.scaling - 60, 150, 40)
        menu_buttons = [
            {"label": "Start Game", "rect": pygame.Rect(self.width * self.scaling // 2 - 100, self.height * self.scaling // 2 - 90, 200, 50)},
            {"label": "Leaderboard", "rect": pygame.Rect(self.width * self.scaling // 2 - 100, self.height * self.scaling // 2 - 20, 200, 50)},
            {"label": "Change Background", "rect": pygame.Rect(self.width * self.scaling // 2 - 100, self.height * self.scaling // 2 + 50, 200, 50)},
            {"label": "Quit", "rect": pygame.Rect(self.width * self.scaling // 2 - 100, self.height * self.scaling // 2 + 120, 200, 50)},
        ]
        bg_buttons = [
            {"label": os.path.basename(path), "rect": pygame.Rect(self.width * self.scaling // 2 - 100, 120 + i * 70, 200, 50), "idx": i}
            for i, path in enumerate(self.background_paths)
        ]
        while self.state != "quit":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = "quit"
                elif self.state == "menu":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for btn in menu_buttons:
                            if btn["rect"].collidepoint(pos):
                                if btn["label"] == "Start Game":
                                    self.restart()
                                elif btn["label"] == "Leaderboard":
                                    self.state = "leaderboard"
                                elif btn["label"] == "Change Background":
                                    self.state = "background"
                                elif btn["label"] == "Quit":
                                    self.state = "quit"
                elif self.state == "background":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for btn in bg_buttons:
                            if btn["rect"].collidepoint(pos):
                                self.set_background(btn["idx"])
                                self.state = "menu"
                        back_rect = pygame.Rect(self.width * self.scaling // 2 - 100, self.height * self.scaling - 60, 200, 40)
                        if back_rect.collidepoint(pos):
                            self.state = "menu"
                elif self.state == "leaderboard":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.state = "menu"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.state in ("playing", "won", "lost"):
                        self.state = "menu"
                    if event.key == pygame.K_r and self.state in ("playing", "won", "lost"):
                        self.restart()
                elif self.state in ("lost", "won"):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_rect.collidepoint(event.pos):
                            self.restart()
                elif self.state == "playing":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        x, y = int(pos[0] / self.scaling), int(pos[1] / self.scaling)
                        if 0 <= x < self.board.width and 0 <= y < self.board.height:
                            if event.button == 1:
                                cell = self.board.grid[x][y]
                                if not cell.flagged:
                                    self.board.reveal_cell(x, y)
                                    if self.board.grid[x][y].is_mine:
                                        self.state = "lost"
                                        self.board.reveal_all_mines()
                                    else:
                                        if self.check_win():
                                            self.win_time = time.time() - self.start_time if self.start_time else 0
                                            self.state = "name_entry"
                            elif event.button == 3:
                                cell = self.board.grid[x][y]
                                if not cell.revealed:
                                    cell.flagged = not cell.flagged
                                    if self.check_win():
                                        self.win_time = time.time() - self.start_time if self.start_time else 0
                                        self.state = "name_entry"
                elif self.state == "name_entry":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and self.player_name:
                            save_leaderboard(self.player_name, self.win_time)
                            self.state = "won"
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        elif len(self.player_name) < 12 and event.unicode.isprintable():
                            self.player_name += event.unicode
            # Draw current screen
            if self.state == "menu":
                draw_menu(screen, menu_font, small_font, self.width, self.scaling, menu_buttons)
            elif self.state == "background":
                draw_background_selection(screen, menu_font, small_font, self.width, self.scaling, bg_buttons)
            elif self.state == "leaderboard":
                entries = load_leaderboard()
                draw_leaderboard(screen, menu_font, small_font, self.width, self.scaling, entries)
            elif self.state == "name_entry":
                draw_name_entry(screen, menu_font, small_font, self.width, self.scaling, self.player_name, self.win_time)
            else:
                screen.blit(self.background, (0, 0))
                self.board.draw_grid_lines(screen, self.scaling)
                self.draw_flags(screen)
                for x in range(self.board.width):
                    for y in range(self.board.height):
                        cell = self.board.grid[x][y]
                        if cell.revealed and not cell.is_mine and cell.neighbor_mines > 0:
                            text = font.render(str(cell.neighbor_mines), True, (0, 0, 0))
                            screen.blit(text, (cell.x * self.scaling + 10, cell.y * self.scaling))
                        elif cell.revealed and cell.is_mine:
                            cx = cell.x * self.scaling + self.scaling // 2
                            cy = cell.y * self.scaling + self.scaling // 2
                            pygame.draw.circle(screen, (0, 0, 0), (cx, cy), self.scaling // 3)
                if self.state == "lost":
                    text = font.render("Game Over", True, (255, 0, 0))
                    rect = text.get_rect(center=(self.width * self.scaling // 2, self.height * self.scaling // 2))
                    screen.blit(text, rect)
                elif self.state == "won":
                    text = font.render("You Win!", True, (0, 180, 0))
                    rect = text.get_rect(center=(self.width * self.scaling // 2, self.height * self.scaling // 2))
                    screen.blit(text, rect)
                if self.state in ("lost", "won"):
                    pygame.draw.rect(screen, (200, 200, 200), button_rect)
                    btn_text = pygame.font.SysFont('arial', 30).render("Restart (R)", True, (0, 0, 0))
                    btn_rect = btn_text.get_rect(center=button_rect.center)
                    screen.blit(btn_text, btn_rect)
                controls = small_font.render("ESC: Menu   R: Restart", True, (80, 80, 80))
                screen.blit(controls, (10, self.height * self.scaling - 30))
            pygame.display.flip()
        pygame.quit()