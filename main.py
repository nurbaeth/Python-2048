import random
import os

SIZE = 4

def init_board():
    return [[0] * SIZE for _ in range(SIZE)]

def add_new_tile(board):
    empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row

def merge(row):
    for i in range(SIZE - 1):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move_left(board):
    for r in range(SIZE):
        board[r] = compress(board[r])
        board[r] = merge(board[r])
        board[r] = compress(board[r])

def move_right(board):
    for r in range(SIZE):
        board[r].reverse()
        move_left(board)
        board[r].reverse()

def move_up(board):
    board[:] = list(map(list, zip(*board)))
    move_left(board)
    board[:] = list(map(list, zip(*board)))

def move_down(board):
    board[:] = list(map(list, zip(*board)))
    move_right(board)
    board[:] = list(map(list, zip(*board)))

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print("\t".join(str(num) if num != 0 else '.' for num in row))
    print()

def check_game_over(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return False
            if c < SIZE - 1 and board[r][c] == board[r][c + 1]:
                return False
            if r < SIZE - 1 and board[r][c] == board[r + 1][c]:
                return False
    return True

def main():
    board = init_board()
    add_new_tile(board)
    add_new_tile(board)
    
    while True:
        print_board(board)
        move = input("Move (WASD): ").strip().upper()
        
        if move == 'W':
            move_up(board)
        elif move == 'A':
            move_left(board)
        elif move == 'S':
            move_down(board)
        elif move == 'D':
            move_right(board)
        else:
            continue
        
        add_new_tile(board)
        
        if check_game_over(board):
            print_board(board)
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
