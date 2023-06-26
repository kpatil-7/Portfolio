# CEO Simulator
This is a simple company simulation game written in Python. The objective of the game is to successfully manage your company for a specified number of months and achieve a winning outcome. The game involves making decisions based on random events and user input, which will affect the status and performance of your company.

## How to Play

1. Run the script to start the game.
2. You will be presented with an introduction and the name of your company.
3. The game consists of several months, and each month you will encounter a random event.
4. Based on the event, you need to make a choice by entering a corresponding action number.
5. After making your choice, the game will update your company's status and provide a revenue report.
6. The game will also check the company's overall status and notify you if any negative conditions occur.
7. The game continues until you reach the end of the specified number of months or encounter a losing condition.
8. If you successfully manage your company without encountering any losing conditions, you win the game!

## Dependencies

This game requires the following dependencies:

- `global_vars.py`: A module containing global variables and classes used in the game.

Make sure to have all the dependencies installed before running the script.

## Running the Game

To run the game, execute the following command:

```shell
python company_simulation.py
```

## Game Outcome

At the end of the game, one of the following outcomes will be displayed:

- If you successfully managed your company without encountering any losing conditions, you will see a winning message.
- If you encountered a losing condition (out of money, product obsolete, customer unhappy, or employee unhappy), you will see the corresponding losing message.

Good luck managing your company and have fun playing the game!
