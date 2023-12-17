from enums import TicTacToeSymbol


class Board:
    def __init__(self) -> None:
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index: int) -> str:
        return self.board[index]

    def __setitem__(self, index: int, symbol: TicTacToeSymbol) -> None:
        self.board[index] = symbol

    # печатаем доску
    def print_board(self) -> None:
        b = self.board
        print(
            f"{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}"
        )


class Player:
    def __init__(self, board: Board, symbol: TicTacToeSymbol) -> None:
        self.current_player = symbol
        self.board = board

    # переход хода
    def switching_players(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    # логика ходов компьютера - не доделана
    def computer_move(self, symbol: TicTacToeSymbol) -> None:
        pass
        # for i in range (len(self.board)):
        #     if symbol == self.board[i]:
        #         self.board.pop(i)
        # possible_moves = self.board
        # move = 0


class Gameplay:
    def __init__(self, board: Board, player: Player) -> None:
        self.board = board
        self.quit = False
        self.player = player

    # проверка на победу или ничью
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
            self.board.print_board()
            return None
        if winner is False and " " not in b:
            self.quit = True
            print("Стоп игра! Ничья...")
            self.board.print_board()
            return None

    # сообщение для игрока
    def show_input_message(self) -> str:
        return "Введите номер от 1 до 9 для выбора ячейки или q для выхода: "

    # ввод номера ячейки или выход от игрока
    def get_input_msg(self, input_msg) -> str | None:
        if input_msg.lower() == "q":
            self.quit = True
            print("Игра прервана")
            return None
        if input_msg not in "123456789" or input_msg == "":
            return self.show_input_message()
        input_msg = int(input_msg) - 1
        if self.board[input_msg] != " ":
            print("Ячейка уже занята, выберите другую: ")
            return None
        else:
            self.board[input_msg] = self.player.current_player
            self.get_winner(self.player.current_player)
            self.player.switching_players()

            return None
