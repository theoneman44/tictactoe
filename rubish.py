
def computer_move(board):
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if is_winner(board_copy, letter):
                move = i
        return move

    corners_open = []
    for i in possible_moves:
    if i in [1, 3, 7, 9]:
    corners_open.append(i)
    if corners_open:
    move = random.choice(corners_open)
    return move

    if 5 in possible_moves:
    move = 5
    return move

    edges_open = []
    for i in possible_moves:
    if i in [2, 4, 6, 8]:
    edges_open.append(i)
    if edges_open:
    move = random.choice(edges_open)

    return move

    # печатаем пустую таблицу
    def print_empty_board(self) -> str:
        empty_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        return f'{empty_board[0:3]}\n-----\n{empty_board[3:6]}\n-----\n{empty_board[6:9]}'
    
        for i in range(1, 10):
            if i not in board.keys():
                board[i] = ' '