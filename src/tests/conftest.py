import pytest
from src.game.enums import TicTacToeSymbol
from src.game.gameplay import Board


@pytest.fixture
def symbol():
    symbol = TicTacToeSymbol
    return symbol


@pytest.fixture
def current_player(symbol):
    return symbol.X


@pytest.fixture
def new_board(symbol):
    new_board = Board()
    new_board.board[0] = symbol.X
    new_board.board[4] = symbol.X
    new_board.board[8] = symbol.X
    return new_board


@pytest.fixture
def draw_board(symbol):
    draw_board = Board()
    for i in [0, 2, 4, 7]:
        draw_board.board[i] = symbol.X
    for i in [1, 3, 5, 6, 8]:
        draw_board.board[i] = symbol.O
    return draw_board


@pytest.fixture
def possible_moves():
    possible_moves = [2, 3, 4, 6, 7, 8]
    return possible_moves


# x 0 x
# 0 x 0
# 0 x 0
