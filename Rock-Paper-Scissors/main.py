# This file control the main loop of pygame
import random
import pygame, sys
import button as btn
import global_vars as G

# First thing in any pygame program - initializes pygame's internal variables.
pygame.init()

# Set window caption
pygame.display.set_caption('Rock Paper Scissor')

# initialize a window with the screen size you set
screen = pygame.display.set_mode(G.SCREEN_SIZE)

# create a clock, which will be used to control the program's frame rate
clock = pygame.time.Clock()

# create rock button
rock_position = (G.SCREEN_WIDTH / 6 - G.BUTTON_WIDTH / 2, 2 * G.SCREEN_HEIGHT / 3)
rockBtn = btn.Button(rock_position, G.BUTTON_SIZE, G.ROCK_IMG)

# create paper button
paper_position = (G.SCREEN_WIDTH / 3 + G.SCREEN_WIDTH / 6 - G.BUTTON_WIDTH / 2, 2 * G.SCREEN_HEIGHT / 3)
paperBtn = btn.Button(paper_position, G.BUTTON_SIZE, G.PAPER_IMG)

# create scissors button
scissors_position = (G.SCREEN_WIDTH / 3*2 + G.SCREEN_WIDTH / 6 - G.BUTTON_WIDTH / 2, 2 * G.SCREEN_HEIGHT / 3)
scissorsBtn = btn.Button(scissors_position, G.BUTTON_SIZE, G.SCISSORS_IMG)

# create upper left display
upper_left_position = (G.SCREEN_WIDTH / 4 - G.DISPLAY_WIDTH / 2, G.SCREEN_HEIGHT / 3)
upperLeftDisplay = btn.Button(upper_left_position, G.DISPLAY_SIZE, G.NONE_IMG)

# create upper right display
upper_right_position = (G.SCREEN_WIDTH / 2 + G.SCREEN_WIDTH / 4 - G.DISPLAY_WIDTH / 2, G.SCREEN_HEIGHT / 3)
upperRightDisplay = btn.Button(upper_right_position, G.DISPLAY_SIZE, G.NONE_IMG)

# create the text display
font = pygame.font.SysFont("Roboto Mono", 32)
text_position = (G.SCREEN_WIDTH / 2, G.SCREEN_HEIGHT / 6)
current_text = G.START_TEXT

# Game control
player_choice = G.NONE
ai_choice = G.NONE


while True:
    # tick forward at 60 frames per second
    clock.tick(60)

    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            sys.exit()
        # Mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # we played already, reset the game
                if player_choice != G.NONE:
                    # Reset the display
                    upperRightDisplay.change_image(G.NONE_IMG)
                    upperLeftDisplay.change_image(G.NONE_IMG)
                    # Reset the text
                    current_text = G.START_TEXT
                    # Reset game state
                    player_choice = G.NONE
                    ai_choice = G.NONE
                # we haven't played
                else:
                    x, y = event.pos
                    if rockBtn.collide(x, y):
                        player_choice = G.ROCK
                    elif paperBtn.collide(x, y):
                        player_choice = G.PAPER
                    elif scissorsBtn.collide(x, y):
                        player_choice = G.SCISSORS
    # Special routine to display
    if player_choice != G.NONE and ai_choice == G.NONE:
        # Get AI choice
        ai_choice = random.randint(0, 2)

        # Update display
        if player_choice == G.ROCK:
            upperLeftDisplay.change_image(G.ROCK_IMG)
        elif player_choice == G.PAPER:
            upperLeftDisplay.change_image(G.PAPER_IMG)
        elif player_choice == G.SCISSORS:
            upperLeftDisplay.change_image(G.SCISSORS_IMG)

        if ai_choice == G.ROCK:
            upperRightDisplay.change_image(G.ROCK_IMG)
        elif ai_choice == G.PAPER:
            upperRightDisplay.change_image(G.PAPER_IMG)
        elif ai_choice == G.SCISSORS:
            upperRightDisplay.change_image(G.SCISSORS_IMG)

        # Check win condition
        if player_choice == ai_choice:
            current_text = G.DRAW_TEXT
        elif (player_choice + 1) % 3 == ai_choice:
            current_text = G.AI_WIN
        else:
            current_text = G.PLAYER_WIN

    # Fill the screen with a solid color
    screen.fill(G.BACKGROUND_COLOR)

    # Draw text
    text = font.render(current_text, True, G.TEXT_COLOR)
    textRect = text.get_rect()
    textRect.center = text_position
    screen.blit(text, textRect)

    # Draw the three buttons
    screen.blit(rockBtn.image, rockBtn.rect)
    screen.blit(paperBtn.image, paperBtn.rect)
    screen.blit(scissorsBtn.image, scissorsBtn.rect)
    screen.blit(upperLeftDisplay.image, upperLeftDisplay.rect)
    screen.blit(upperRightDisplay.image, upperRightDisplay.rect)

    # At the end of each game loop, call pygame.display.flip() to update the screen with what you drew.
    pygame.display.flip()