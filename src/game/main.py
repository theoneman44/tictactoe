from enums import TicTacToeSymbol
from gameplay import Board, Gameplay


def main():
    board = Board()
    symbol = TicTacToeSymbol
    gameplay = Gameplay(board, symbol.X.value)
    while gameplay.quit is False:
        board.print_board()
        if gameplay.current_player == symbol.X.value:
            input_msg = input(gameplay.show_input_message())
            gameplay.get_input_msg(input_msg)


if __name__ == "__main__":
    main()
