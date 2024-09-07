from constants import Player_O, Player_X
import os
import json

#Board
class Board:

    def __init__(self) -> None:
        #Crear el board, especificamente los espacios que los jugadores elijiran para jugar X o 0. 
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        #El display del board son los separadores de los espacios en los que se juegan los simbolos, para ver el tablero.
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def update(self, row, col, player_symbol):
        #función que reemplaza los espacios creados en el init por la jugada del jugador
        if self.board[row][col] == " ":
            self.board[row][col] = player_symbol
            return True
        else: 
            print("Este espacio ya está ocupado!")
            return False
        
    def check_winner(self, player_symbol):
        #Verifica si el jugador ganó horizontalmente
        for row in self.board:
            if all([spot == player_symbol for spot in row]):
                return True
        #Verifica si el jugador ganó verticalmente
        for col in range(3):
            if all([self.board[row][col] == player_symbol for row in range(3)]):
                return True
        #Verifica si el jugador ganó diagonalmente, de izquierda a derecha 
        if all([self.board[i][i] == player_symbol for i in range(3)]) or \
            all([self.board[i][2 - i] == player_symbol for i in range(3)]):
        #Verifica si el jugador ganó diagonalmente, de derecha a izquierda
            return True   
        return False     

    def is_full(self):
        #Verifica si el tablero está lleno
        return all([spot != " " for row in self.board for spot in row])
#Jugador
class Player:

    def __init__(self, symbol):
        self.symbol = symbol
        #Define el jugador como una variable simbolo, el cual será asignado luego

    def make_move(self, board):

        while True:
            try:
                row = int(input(f"Jugador {self.symbol}, elija la fila (0, 1, or 2): "))
                col = int(input(f"Jugador {self.symbol}, elija la columna (0, 1 o 2): "))
                if board.update(row, col, self.symbol):
                    break
                else:
                    print("Movimiento invalido, intente de nuevo.")
            except ValueError:
                print("Ingrese un número valido")
#Juego
class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = Player(Player_X)
        self.player2 = Player(Player_O)
        self.current_player = self.player1

    def save_game(self, result):

        file_path = os.path.join(os.path.dirname(__file__), "tictactoe_history.json")

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump({"Victorias de X": 0, "Victorias de O": 0, "Empates": 0}, file)

        with open (file_path, "r") as file:
            history = json.load(file)

        if result == "X gana":
            history["Victorias de X"] += 1
        elif result == "O gana":
            history["Victorias de O"] += 1
        elif result == "Empate":
            history["Empates"] += 1
        
        with open (file_path, "w") as file:
            json.dump(history, file)

    def switch_player(self):

        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):

        while True:

            self.board.display()
            self.current_player.make_move(self.board)
            
            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"El jugador {self.current_player.symbol} gana!")
                self.save_game(f"{self.current_player.symbol} gana")
                break

            if self.board.is_full():
                self.board.display()
                print("El tablero se ha llenado, es un empate!")
                self.save_game("Empate")
                break

            self.switch_player()
#iniciar juego
def init_game():
    game = Game()
    game.play()
    
            