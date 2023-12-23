from enums import TicTacToeSymbol
from gameplay import Board, Gameplay


def main():
    board = Board()
    symbol = TicTacToeSymbol
    gameplay = Gameplay(board, symbol.X)
    board.print_board()
    while not gameplay.quit:
        if gameplay.current_player == symbol.X:
            input_msg = input(gameplay.show_input_message())
            gameplay.get_input_msg(input_msg)
        if gameplay.current_player == symbol.O:
            gameplay.computer_move(symbol.O)
        board.print_board()


if __name__ == "__main__":
    main()
