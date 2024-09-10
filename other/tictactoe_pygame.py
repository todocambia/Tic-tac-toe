import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

# Board positions (grid mapping)
board_mapping = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2)
}

# Create the board
class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def draw(self, screen):
        # Draw the grid
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 10)
        pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 10)
        pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 10)
        pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 10)

        # Draw X and O marks
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    self.draw_x(screen, row, col)
                elif self.board[row][col] == "O":
                    self.draw_o(screen, row, col)

    def draw_x(self, screen, row, col):
        pygame.draw.line(screen, RED, (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), 10)
        pygame.draw.line(screen, RED, (col * 200 + 150, row * 200 + 50), (col * 200 + 50, row * 200 + 150), 10)

    def draw_o(self, screen, row, col):
        pygame.draw.circle(screen, BLUE, (col * 200 + 100, row * 200 + 100), 50, 10)

    def update(self, row, col, player_symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = player_symbol
            return True
        return False

    def check_winner(self, player_symbol):
        # Check rows and columns
        for row in range(3):
            if all([self.board[row][col] == player_symbol for col in range(3)]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player_symbol for row in range(3)]):
                return True
        # Check diagonals
        if all([self.board[i][i] == player_symbol for i in range(3)]) or \
                all([self.board[i][2 - i] == player_symbol for i in range(3)]):
            return True
        return False

    def is_full(self):
        return all([spot != " " for row in self.board for spot in row])

# Draw the menu
def draw_menu(screen):
    screen.fill(GRAY)
    title = font.render("🎮 Tic Tac Toe 🎮", True, BLACK)
    start_game_text = small_font.render("1 - Start Game", True, BLACK)
    controls_text = small_font.render("2 - Controls", True, BLACK)
    quit_text = small_font.render("3 - Quit", True, BLACK)

    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(start_game_text, (SCREEN_WIDTH // 2 - start_game_text.get_width() // 2, 250))
    screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, 300))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 350))
    pygame.display.flip()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 60)
small_font = pygame.font.Font(None, 40)

# Board positions (grid mapping)
board_mapping = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2)
}

# Create the board
class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def draw(self, screen):
        # Draw the grid
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 10)
        pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 10)
        pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 10)
        pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 10)

        # Draw X and O marks
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "X":
                    self.draw_x(screen, row, col)
                elif self.board[row][col] == "O":
                    self.draw_o(screen, row, col)

    def draw_x(self, screen, row, col):
        pygame.draw.line(screen, RED, (col * 200 + 50, row * 200 + 50), (col * 200 + 150, row * 200 + 150), 10)
        pygame.draw.line(screen, RED, (col * 200 + 150, row * 200 + 50), (col * 200 + 50, row * 200 + 150), 10)

    def draw_o(self, screen, row, col):
        pygame.draw.circle(screen, BLUE, (col * 200 + 100, row * 200 + 100), 50, 10)

    def update(self, row, col, player_symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = player_symbol
            return True
        return False

    def check_winner(self, player_symbol):
        # Check rows and columns
        for row in range(3):
            if all([self.board[row][col] == player_symbol for col in range(3)]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player_symbol for row in range(3)]):
                return True
        # Check diagonals
        if all([self.board[i][i] == player_symbol for i in range(3)]) or \
                all([self.board[i][2 - i] == player_symbol for i in range(3)]):
            return True
        return False

    def is_full(self):
        return all([spot != " " for row in self.board for spot in row])

# Draw the menu
def draw_menu(screen):
    screen.fill(GRAY)
    title = font.render("🎮 Tic Tac Toe 🎮", True, BLACK)
    start_game_text = small_font.render("1 - Start Game", True, BLACK)
    controls_text = small_font.render("2 - Controls", True, BLACK)
    quit_text = small_font.render("3 - Quit", True, BLACK)

    screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(start_game_text, (SCREEN_WIDTH // 2 - start_game_text.get_width() // 2, 250))
    screen.blit(controls_text, (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, 300))
    screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 350))
    pygame.display.flip()

def draw_controls(screen):
    screen.fill(GRAY)
    
    # Define colors and fonts
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRID_COLOR = (0, 0, 0)
    
    # Define grid parameters
    cell_size = 100
    board_start_x = SCREEN_WIDTH // 2 - cell_size * 1.5
    board_start_y = SCREEN_HEIGHT // 2 - cell_size * 1.5

    # Draw the grid
    for row in range(4):
        pygame.draw.line(screen, GRID_COLOR, 
                         (board_start_x, board_start_y + row * cell_size), 
                         (board_start_x + 3 * cell_size, board_start_y + row * cell_size), 2)
    for col in range(4):
        pygame.draw.line(screen, GRID_COLOR, 
                         (board_start_x + col * cell_size, board_start_y), 
                         (board_start_x + col * cell_size, board_start_y + 3 * cell_size), 2)
    
    # Define control key mappings
    controls = {
        "q": (0, 0), "w": (0, 1), "e": (0, 2),
        "a": (1, 0), "s": (1, 1), "d": (1, 2),
        "z": (2, 0), "x": (2, 1), "c": (2, 2)
    }
    
    # Draw control keys
    font = pygame.font.Font(None, 36)
    for key, (row, col) in controls.items():
        text = font.render(key, True, BLACK)
        text_rect = text.get_rect(center=(board_start_x + col * cell_size + cell_size // 2,
                                          board_start_y + row * cell_size + cell_size // 2))
        screen.blit(text, text_rect)

    # Draw the prompt at the bottom
    prompt = font.render("Press any key to return", True, BLACK)
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    screen.blit(prompt, prompt_rect)
    
    pygame.display.flip()
    
    # Wait for a key press to go back to the main menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False  # Exit loop after key press


# Display end game message
def draw_end_message(screen, message):
    screen.fill(GRAY)
    end_message = font.render(message, True, BLACK)
    screen.blit(end_message, (SCREEN_WIDTH // 2 - end_message.get_width() // 2, SCREEN_HEIGHT // 2 - end_message.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before returning to the menu

# Main game loop
def game_loop(screen):
    board = Board()
    current_player = "X"
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                key = pygame.key.name(event.key)
                if key in board_mapping:
                    row, col = board_mapping[key]
                    if board.update(row, col, current_player):
                        if board.check_winner(current_player):
                            draw_end_message(screen, f"Player {current_player} wins!")
                            game_over = True
                        elif board.is_full():
                            draw_end_message(screen, "It's a draw!")
                            game_over = True
                        current_player = "O" if current_player == "X" else "X"
        
        board.draw(screen)
        pygame.display.flip()

# Menu loop
def menu_loop(screen):
    while True:
        draw_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key == '1':
                    game_loop(screen)
                elif key == '2':
                    draw_controls(screen)
                elif key == '3':
                    pygame.quit()
                    sys.exit()

# Set up the screen and start the menu loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

menu_loop(screen)


# Display end game message
def draw_end_message(screen, message):
    screen.fill(GRAY)
    end_message = font.render(message, True, BLACK)
    screen.blit(end_message, (SCREEN_WIDTH // 2 - end_message.get_width() // 2, SCREEN_HEIGHT // 2 - end_message.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before returning to the menu

# Main game loop
def game_loop(screen):
    board = Board()
    current_player = "X"
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not game_over:
                key = pygame.key.name(event.key)
                if key in board_mapping:
                    row, col = board_mapping[key]
                    if board.update(row, col, current_player):
                        if board.check_winner(current_player):
                            draw_end_message(screen, f"Player {current_player} wins!")
                            game_over = True
                        elif board.is_full():
                            draw_end_message(screen, "It's a draw!")
                            game_over = True
                        current_player = "O" if current_player == "X" else "X"
        
        board.draw(screen)
        pygame.display.flip()

# Menu loop
def menu_loop(screen):
    while True:
        draw_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key == '1':
                    game_loop(screen)
                elif key == '2':
                    draw_controls(screen)
                elif key == '3':
                    pygame.quit()
                    sys.exit()

# Set up the screen and start the menu loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

menu_loop(screen)
