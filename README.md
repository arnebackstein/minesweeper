# Minesweeper

A modular, Pygame-based Minesweeper game with menu, leaderboard, and customizable backgrounds.


## Project Structure

- [`main.py`](main.py): Entry point, initializes and starts the game.
- [`game.py`](game.py): Main game logic, state management, and event loop.
- [`board.py`](board.py): Board logic, mine placement, cell revealing.
- [`cell.py`](cell.py): Cell data structure.
- [`leaderboard.py`](leaderboard.py): Leaderboard file I/O and sorting.
- [`ui.py`](ui.py): Menu, background selection, leaderboard, and name entry UI rendering.
- [`background_imgs/`](background_imgs/): Place background images here (jpg, png).

## Requirements

- Python 3.8+
- pygame

## Setup

```sh
pip install pygame
```

## Usage

```sh
python main.py
```

- Use the menu to start a game, view leaderboard, or change background.
- After winning, enter your name to save your time to the leaderboard.
- Add images to `background_imgs/` to expand background options.

## Controls

- Left click: Reveal cell
- Right click: Flag/unflag cell
- R: Restart game
- ESC: Return to menu

## License

MIT License