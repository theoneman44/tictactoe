import random
from enums import TicTacToeSymbol


class Board:
    def __init__(self) -> None:
        self.symbol = TicTacToeSymbol
        self.empty_cell = self.symbol.empty.value
        self.board = [
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
            self.empty_cell,
        ]

    def __getitem__(self, index: int) -> str:
        return self.board[index]

    def __setitem__(self, index: int, symbol: TicTacToeSymbol) -> None:
        self.board[index] = symbol

    def print_board(self) -> None:
        b = self.board
        print(
            f"{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}"
        )

    def possible_moves(self) -> list[int]:
        possible_moves = []
        for i in range(len(self.board)):
            if self.board[i] == self.empty_cell:
                possible_moves.append(i + 1)
        return possible_moves


class Gameplay:
    def __init__(self, board: Board, symbol: TicTacToeSymbol) -> None:
        self.board = board
        self.quit = False
        self.current_player = symbol
        self.symbol_O = self.board.symbol.O.value
        self.symbol_X = self.board.symbol.X.value

    def get_winner(self, symbol: TicTacToeSymbol) -> None:
        b = self.board
        winner = (
            (b[0] == b[1] == b[2] == symbol)
            or (b[3] == b[4] == b[5] == symbol)
            or (b[6] == b[7] == b[8] == symbol)
            or (b[0] == b[3] == b[6] == symbol)
            or (b[1] == b[4] == b[7] == symbol)
            or (b[2] == b[5] == b[8] == symbol)
            or (b[0] == b[4] == b[8] == symbol)
            or (b[2] == b[4] == b[6] == symbol)
        )
        if winner is True:
            self.quit = True
            print(f"Стоп игра! Выиграли {symbol}.")
        elif self.board.empty_cell not in b:
            self.quit = True
            print("Стоп игра! Ничья...")
        return None

    def switching_players(self) -> None:
        self.current_player = self.symbol_O if self.current_player == self.symbol_X else self.symbol_X

    def show_input_message(self) -> str:
        return "Введите номер от 1 до 9 для выбора ячейки или q для выхода: "

    def get_input_msg(self, input_msg: str) -> str | None:
        if input_msg.lower() == "q":
            self.quit = True
            print("Игра прервана")
            return None
        if input_msg not in "123456789" or input_msg == "":
            return self.show_input_message()
        input_msg = int(input_msg) - 1
        if self.board[input_msg] != self.board.empty_cell:
            print("Ячейка уже занята, выберите другую: ")
            return None
        else:
            self.board[input_msg] = self.current_player
            self.get_winner(self.current_player)
            self.switching_players()

            return None

    def computer_move(self, symbol: TicTacToeSymbol) -> None:
        possible_moves = self.board.possible_moves()

        if len(possible_moves) > 1 and self.quit is False:
            move = random.choice(possible_moves)
            self.board[move - 1] = symbol
            self.get_winner(self.current_player)
            self.switching_players()
            print(f"Ход компьютера: {move}")
        return None
