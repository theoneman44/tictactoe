import pytest
from src.game.gameplay import Gameplay


def test__possible_moves(new_board, possible_moves, current_player):
    gameplay = Gameplay(new_board, current_player)
    assert gameplay.board.possible_moves() == possible_moves


def test__get_winner__winner(new_board, current_player):
    gameplay = Gameplay(new_board, current_player)
    gameplay.get_winner(current_player)
    assert gameplay.quit is True


def test__get_winner__draw(draw_board, current_player):
    gameplay = Gameplay(draw_board, current_player)
    gameplay.get_winner(current_player)
    assert gameplay.quit is True


def test__switching_players(new_board, current_player, symbol):
    gameplay = Gameplay(new_board, current_player)
    gameplay.switching_players()
    assert gameplay.current_player == symbol.O


@pytest.mark.parametrize('input_msg,expected',
                         [('q', 'Игра прервана'),
                          ('25', None),
                          ('', None),
                          ('1', 'Ячейка уже занята, выберите другую.'),
                          ('6', 5)])
def test__handle_input_msg(input_msg, expected, new_board, symbol):
    gameplay = Gameplay(new_board, symbol.X)
    assert gameplay.handle_input_msg(input_msg) == expected


def test__computer_move(new_board, symbol):
    gameplay = Gameplay(new_board, symbol.O)
    gameplay.computer_move(symbol.O)
    assert symbol.O in gameplay.board
