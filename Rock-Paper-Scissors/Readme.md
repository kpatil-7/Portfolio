# Rock Paper Scissors

Welcome to Rock Paper Scissors! This repository contains a Python implementation of the classic game with a simple graphical user interface (GUI).

## How to Play

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the cloned repository directory.

### Running the Game

1. Run the `main.py` file using the following command:

   ```shell
   python main.py
   ```

2. The game window will open, displaying buttons for rock, paper, and scissors.

3. Click on the button corresponding to your chosen move.

4. The AI player will randomly select its move, and the result will be displayed on the screen.

5. If you want to play again, simply click on another button.

### Repository Structure

- `main.py`: This file controls the main loop of the game. It initializes the game window, handles user input, updates the display, and determines the winner.
- `button.py`: This file defines the `Button` class used for creating buttons in the GUI. It handles button positioning, collision detection, and image rendering.
- `global_vars.py`: This file contains global variables and constants used in the game, including screen size, button size, image paths, and text strings.

## Dependencies

This game relies on the following Python packages:

- `pygame`: A Python library for creating games and multimedia applications.
- `sys`: A module providing access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

You can install the `pygame` dependency using `pip` with the following command:

```shell
pip install pygame
```

## Contributions

Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.
