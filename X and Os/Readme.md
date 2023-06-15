# X and Os

Welcome to X and Os, a classic game of tic-tac-toe implemented in Python! This repository allows you to play the game either against an AI or against another player.

## How to Play

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the cloned repository directory.

### Against AI

1. Run the `main.py` file using the following command:

   ```shell
   python main.py
   ```

2. You will be prompted to choose a game mode. Enter `1` to play against the AI.

3. The game will display an empty 3x3 grid. Players take turns placing their markers (X or O) on the grid.

4. To make a move, you will be asked to enter the coordinates of the cell where you want to place your marker. The coordinates should be provided in the format `row,column`, where both `row` and `column` are integers between 0 and 2. For example, to place your marker in the top-left cell, enter `0,0`.

5. The game will continue until a player wins or the board is filled, resulting in a tie. If you want to play again, simply run the `main.py` file again.

### Against Another Player

1. Run the `main.py` file using the following command:

   ```shell
   python main.py
   ```

2. You will be prompted to choose a game mode. Enter `2` to play against another player.

3. The game will display an empty 3x3 grid. Players take turns placing their markers (X or O) on the grid.

4. To make a move, players will be asked to enter the coordinates of the cell where they want to place their marker. The coordinates should be provided in the format `row,column`, where both `row` and `column` are integers between 0 and 2. For example, to place a marker in the top-left cell, enter `0,0`.

5. The game will continue until a player wins or the board is filled, resulting in a tie. If you want to play again, simply run the `main.py` file again.

## Repository Structure

- `main.py`: The main entry point of the game. It handles user input and controls the flow of the game.
- `ai.py`: This file contains the logic for the AI player. It determines the AI's moves based on the current state of the board.
- `move.py`: This file provides functions for validating and processing player moves. It handles the conversion of input coordinates to the appropriate indices in the board grid.
- `board.py`: This file defines the `Board` class, which represents the game board. It handles the display of the board and the checking of win conditions.

## Contributions

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.
