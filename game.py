#imports
import pygame
from grid import Board
from dictionary import colors

#initialize pygame
pygame.init()

# setup of pygame display width, timers, and font defaults
screen = pygame.display.set_mode([400, 500])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)


# game variables initialize
game_board = Board(4)
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = game_board.score

#open high score value, for display
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high



def draw_pieces(b):
    """
    Description: draws the numpy board onto the pygmae.

    Inputs:  The numpy array, stored as a grid here

    Returns: nothing, but does draw the pieces onto the pygame board

    """
    for i in range(4):
        for j in range(4):
            value = b[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)



def draw_over():
    """
    Description: Draws over the previous iteration of the pygame.  Done
    done when a move is made that results in the game ending.
    Draws over the board with instructions to restart and the game over
    texts.

    Inputs: None

    Returns: Nothing, but draws over the pygame and addresses the 
    endgame functionality when applicable.  Handles only the endgame
    instructions

    """
    #create background black rectangle for players to visually see text easier
    pygame.draw.rect(screen, (128, 0, 128), [50, 50, 300, 100], 0, 10)

    #create output text
    restartText = font.render('Press Enter to Restart', True, 'white')
    endgameText = font.render('Game Over!', True, 'white')

    #output texts onto screen
    screen.blit(restartText, (70, 105))
    screen.blit(endgameText, (130, 65))


def draw_board():
    """
    Description: draws the basic background of the board.  This contains:

        1. the brown background of the board
        2. the high score from the high score file
        3. the current score that the user is playing with

    done after each turn when applicable

    Inputs: None

    Returns: Nothing, but has the pygame display having a drawn board background,
    high score and score at the bottom of the display.

    """

    #use the board game color to color the background of the pygame
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)

    #as before, create the text high score
    textScore = font.render(f'Score: {game_board.score}', True, 'black')
    textHighScore = font.render(f'High Score: {high_score}', True, 'black')

    #draw the high score and score over the display background
    screen.blit(textHighScore, (10, 450))
    screen.blit(textScore, (10, 410))
    pass


if __name__ == '__main__':
    # main game loop
    run = True
    while run:
        timer.tick(fps)
        screen.fill('gray')
        draw_board()
        game_grid = game_board.grid
        draw_pieces(game_grid)
        if spawn_new or init_count < 2:
            game_grid, game_over = game_board.new_pieces()
            spawn_new = False
            init_count += 1
        if direction != '':
            game_grid = game_board.take_turn(direction)
            direction = ''
            spawn_new = True
        if game_over:
            draw_over()
            if high_score > init_high:
                file = open('high_score', 'w')
                file.write(f'{high_score}')
                file.close()
                init_high = high_score

        #movement event and game restart event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    direction = 'UP'
                elif event.key == pygame.K_DOWN:
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    direction = 'RIGHT'

                #if game over, then the return value is the only valid key
                if game_over:
                    if event.key == pygame.K_RETURN:
                        game_board = Board(4)
                        spawn_new = True
                        init_count = 0
                        score = game_board.score
                        direction = ''
                        game_over = False

        if game_board.score > high_score:
            high_score = game_board.score

        pygame.display.flip()
    pygame.quit()



