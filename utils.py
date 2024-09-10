from constants import Player_O, Player_X
import os
import json

#Tablero
class Board:

    def __init__(self) -> None:
        #Crear el board, especificamente los espacios que los jugadores elijiran para jugar X o 0. 
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        top_border = "╔═══╦═══╦═══╗"
        middle_border = "╠═══╬═══╬═══╣"
        bottom_border = "╚═══╩═══╩═══╝"
        board_lines = [top_border]
        for i, row in enumerate(self.board):
            row_str = f" {row[0]} " + "║" + f" {row[1]} " + "║" + f" {row[2]} "
            board_lines.append(f"║{row_str}║")
            if i < 2:  
                board_lines.append(middle_border)
        board_lines.append(bottom_border)
        board_display = "\n".join(board_lines)
        print(board_display)

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
        controles = {
            "q": (0,0), "w": (0,1), "e": (0,2),
            "a": (1,0), "s": (1,1), "d": (1,2),
            "z": (2,0), "x": (2,1), "c": (2,2)
        }
        while True:
            print("\n")
            jugada = input(f"Jugador {self.symbol}, elija su movimiento usando el teclado:").lower()
            print("\n")
            if jugada in controles:
                row, col = controles[jugada]
                if board.update(row, col, self.symbol):
                    break
                else:
                    print("Este espacio ya está ocupado")
            else:
                print("Movimiento invalido, elija una tecla valida.")
#Menu
class Menu:

    def __init__(self):
        self.menu = Menu

    def options(self):  
        text = """\n\n\n\n
        ╔════════════════════════════════════════════╗
        ║      X       🎮 Tic Tac Toe 🎮       O     ║
        ╠════════════════════════════════════════════╣
        ║                                            ║
        ║            1 - Empezar Juego               ║
        ║                                            ║
        ║            2 - Historial                   ║
        ║                                            ║
        ║            3 - Controles                   ║
        ║                                            ║
        ║            4 - Salir del juego             ║
        ║                                            ║
        ╚════════════════════════════════════════════╝
        \n\n   """

        return text 

    def menu_select(self):
        try:    
            eleccion = int(input(self.options()))
            if eleccion < 1 or eleccion > 3:
                print("\n⚠️ Por favor elija una opción valida ⚠️")
                return self.options
            return eleccion
        except ValueError:
            print("\n⚠️ Por favor solo ingresar números. ⚠️")
            return self.options
        
    def mostrar_controles(self):
        controles_board = """
        \nTeclado:\n
        ╔═══╦═══╦═══╗
        ║ q ║ w ║ e ║
        ╠═══╬═══╬═══╣
        ║ a ║ s ║ d ║
        ╠═══╬═══╬═══╣
        ║ z ║ x ║ c ║
        ╚═══╩═══╩═══╝
        \n
        """
        print(controles_board)
        input("Presione cualquier tecla para volver al menu... ")
#Guardar historial de juegos
class GuardarJuego:

    def __init__(self, file_path="tictactoe_history.json"):
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump({"juegos": []}, file)

    def save_game(self, result):
        file_path = os.path.join(os.path.dirname(__file__), "tictactoe_history.json")
        with open(file_path, "r") as file:
            history = json.load(file)
        history["juegos"].append(result)
        with open(file_path, "w") as file:
            json.dump(history, file)

    def mostrar_historial(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
        historial = """
        ╔════════════════════════════════════════════╗
        ║           🎮 Historial de Juegos 🎮        ║
        ╠════════════════════════════════════════════╣
        ║                                            ║
    """
        if not data.get("juegos"):
            historial += "    ║        No hay juegos guardados aún.        ║\n"
        else:
            for idx, juego in enumerate(data["juegos"], 1):
                historial += f"    ║  {idx}. {juego.ljust(39)}║\n"
        historial += """        ║                                            ║
        ╚════════════════════════════════════════════╝\n
    """
        print(historial)
        input("Presione cualquier tecla para volver al menu... ")
#Juego
class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = Player(Player_X)
        self.player2 = Player(Player_O)
        self.current_player = self.player1
        self.guardar = GuardarJuego()

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        while True:
            self.board.display()
            self.current_player.make_move(self.board)
            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"\nEl jugador {self.current_player.symbol} gana!")
                self.guardar.save_game(f"{self.current_player.symbol} gana")
                break
            if self.board.is_full():
                self.board.display()
                print("\nEl tablero se ha llenado, es un empate!")
                self.guardar.save_game("Empate")
                break
            self.switch_player()
#iniciar
def init_game():
    menu = Menu()
    guardar = GuardarJuego()
    while True:
        eleccion = menu.menu_select()
        if eleccion == 1:
            game = Game()
            game.play()
        elif eleccion ==2:
            guardar.mostrar_historial()
        elif eleccion ==3:
            menu.mostrar_controles()
        elif eleccion == 4:
            print("Gracias por jugar. Saliendo del juego...")
            break
        


    
            