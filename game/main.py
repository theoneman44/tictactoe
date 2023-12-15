from enums import TicTacToeSymbol
from gameplay import Board, Gameplay, Player


def main():
    board = Board()
    symbol = TicTacToeSymbol
    player = Player(board, symbol.X.value)
    gameplay = Gameplay(board, player)
    while gameplay.quit is False:
        board.print_board()
        input_msg = input(gameplay.show_input_message())
        gameplay.get_input_msg(input_msg)
        player.computer_move(symbol.O)


if __name__ == '__main__':
    main()
