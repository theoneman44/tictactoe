from .enums import TicTacToeSymbol
from .gameplay import Board, Gameplay


def main() -> None:
    board = Board()
    symbol = TicTacToeSymbol
    gameplay = Gameplay(board, symbol.X)
    board.print_board()
    while not gameplay.quit:
        if gameplay.current_player == symbol.X:
            input_msg = input('Введите номер от 1 до 9 для выбора ячейки или q для выхода: ')
            human_move = gameplay.handle_input_msg(input_msg)
            if type(human_move) is int:
                board[human_move] = symbol.X
                gameplay.get_winner(gameplay.current_player)
                gameplay.switching_players()
        elif gameplay.current_player == symbol.O:
            gameplay.computer_move(symbol.O)
            board.print_board()
            gameplay.get_winner(gameplay.current_player)
            gameplay.switching_players()


if __name__ == '__main__':
    main()
