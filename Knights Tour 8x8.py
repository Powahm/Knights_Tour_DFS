#Only prints final 3 steps, not the intermediate steps, check 6x6 board for full search
chessboard = [[1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

path = [[0, 0]]
x = path[0][0]
y = path[0][1]
same = []
number = 2

def print_chessboard():
    for i in range (8):
        for j in range (8):
            print(chessboard[i][j], end=" ")
        print ("\n")
def possible_moves(x,y):
    global chessboard
    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = []

    for i in range(8):
        # restrictions
        x_values = 0 <= x + pos_x[i] <= 7
        y_values = 0 <= y + pos_y[i] <= 7

        if x_values and y_values and chessboard[x + pos_x[i]][y + pos_y[i]] == 0:
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities



def reset_board():
    global x, y, chessboard, number

    chessboard = [[1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    number = 1

    for o in path:
        q = o[0]
        w = o[1]
        chessboard[q][w] = number
        number += 1
        x = q
        y = w

    print("From Last Checkpoint:")
    print_chessboard()
def warnsdorffs_rule():
    global path, x, y, chessboard, same, reset_path, number
    reset_path = []

    for i in range(63):
        pos = possible_moves(x,y)

        if not pos:
            continue
        else:
            mini = pos[0]

            for p in pos:
                if len(possible_moves(p[0],p[1])) < len(possible_moves(mini[0],mini[1])):
                    mini = p
                elif len(possible_moves(p[0],p[1])) == len(possible_moves(mini[0],mini[1])) and possible_moves(p[0],p[1]) != possible_moves(mini[0], mini[1]):
                    reset_path = path.copy()
                    reset_path.append(p)
                    same.append(reset_path)
                    reset_path = []

            x = mini[0]
            y = mini[1]
            path.append([mini[0],mini[1]])

            if chessboard[x][y] == 0:
                chessboard[x][y] = number
                number += 1
                ###print("---Next Move---")
                ###print_chessboard()
            else:
                break

    print("Path: ", path)

run = 1

while run == 1:
    warnsdorffs_rule()

    if path[-1] == [2,1] or path [-1] == [1,2]:
        print_chessboard()
        run += 1
    else:
        print("-----------------redo------------")
        x = same[-1][-1][0]
        y = same[-1][-1][1]
        path = same[-1]
        del same[-1]
        reset_board()
