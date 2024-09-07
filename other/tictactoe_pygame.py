import pygame
import sys

# Constants
SCREEN_SIZE = 300
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Game board class
class Board:

    def __init__(self):
        self.board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    def display(self):
        # Draw vertical lines
        pygame.draw.line(screen, LINE_COLOR, (SCREEN_SIZE // 3, 0), (SCREEN_SIZE // 3, SCREEN_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (2 * SCREEN_SIZE // 3, 0), (2 * SCREEN_SIZE // 3, SCREEN_SIZE), LINE_WIDTH)
        # Draw horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SCREEN_SIZE // 3), (SCREEN_SIZE, SCREEN_SIZE // 3), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 2 * SCREEN_SIZE // 3), (SCREEN_SIZE, 2 * SCREEN_SIZE // 3), LINE_WIDTH)

    def update(self, row, col, player_symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = player_symbol
            return True
        return False

    def check_winner(self, player_symbol):
        # Check rows, columns, and diagonals
        for row in self.board:
            if all([spot == player_symbol for spot in row]):
                return True
        for col in range(BOARD_COLS):
            if all([self.board[row][col] == player_symbol for row in range(BOARD_ROWS)]):
                return True
        if all([self.board[i][i] == player_symbol for i in range(BOARD_ROWS)]) or \
           all([self.board[i][BOARD_COLS - 1 - i] == player_symbol for i in range(BOARD_ROWS)]):
            return True
        return False

    def is_full(self):
        return all([spot != " " for row in self.board for spot in row])

# Draw the X and O symbols
def draw_figures(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SCREEN_SIZE / 3 + SCREEN_SIZE / 6), int(row * SCREEN_SIZE / 3 + SCREEN_SIZE / 6)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SCREEN_SIZE // 3 + SPACE, row * SCREEN_SIZE // 3 + SPACE), (col * SCREEN_SIZE // 3 + SCREEN_SIZE // 3 - SPACE, row * SCREEN_SIZE // 3 + SCREEN_SIZE // 3 - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SCREEN_SIZE // 3 + SPACE, row * SCREEN_SIZE // 3 + SCREEN_SIZE // 3 - SPACE), (col * SCREEN_SIZE // 3 + SCREEN_SIZE // 3 - SPACE, row * SCREEN_SIZE // 3 + SPACE), CROSS_WIDTH)

# Game class
class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1
        self.game_over = False

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]  # X coordinate
                    mouseY = event.pos[1]  # Y coordinate

                    clicked_row = mouseY // (SCREEN_SIZE // 3)
                    clicked_col = mouseX // (SCREEN_SIZE // 3)

                    if self.board.update(clicked_row, clicked_col, self.current_player):
                        draw_figures(self.board.board)
                        if self.board.check_winner(self.current_player):
                            print(f"Player {self.current_player} wins!")
                            self.game_over = True
                        elif self.board.is_full():
                            print("It's a draw!")
                            self.game_over = True
                        self.switch_player()

            pygame.display.update()

# Main loop to start the game
def init_game():
    game = Game()
    game.board.display()
    game.play()

if __name__ == "__main__":
    init_game()
