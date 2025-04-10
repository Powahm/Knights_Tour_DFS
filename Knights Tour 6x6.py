#Starting Chessboard
chessboard = [[1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]


'''
Each vertex is marked by an integer, in this case mainly 0s. The values that take each vertex is the move order of the
knight in the closed knights tour. The starting square is (0,0) therefore it has the number 1 in the default matrix
'''

def possible_moves(x,y): #function that looks at the given vertex and returns values of other vertices that a knight could move to, under knight's tour conditions
    global chessboard

    pos_x = (2, 1, 2, 1, -2, -1, -2, -1)
    pos_y = (1, 2, -1, -2, 1, 2, -1, -2)
    possibilities = [] #list that will hold the possible vertices the knight could move to

    for i in range(8): #for loop that is bounded to 8, as 8 is the max. amount of moves a knight can move to
        # restrictions for the knight. This ensures that the knight move is within the chessboard
        x_values = 0 <= x + pos_x[i] <= 5
        y_values = 0 <= y + pos_y[i] <= 5

        if x_values and y_values and chessboard[x + pos_x[i]][y + pos_y[i]] == 0: #checks if the move is within chessboard and is an empty square
            possibilities.append([x + pos_x[i], y + pos_y[i]])

    return possibilities #returns a list of the moves that a knight could take

path = [[0, 0]] #list that will hold the final path coordinates for a closed knight's tour
x = path[0][0] #intital x value on matrix (0)
y = path[0][1] #intital y value on matrix (0)
same = [] #list that serves as a DFS tree but represented here as a multi-layered list
number = 2 #variable that always has integer values. It is used to mark each vertex with knight move order

def reset_board():
    #function that resets the board to the last checkpoint using the last element in the "same" list
    global x, y, chessboard, number
    chessboard = [[1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]

    number = 1
    print("Reset board path", path)

    for o in path:
        q = o[0]
        w = o[1]
        chessboard[q][w] = number
        number += 1
        x = q
        y = w
    print("From Last Checkpoint:")
    print_chessboard()
def warnsdorffs_rule(): #function that uses principles of the Warnsdorff's rule to choose the correct knight move

    global path, x, y, chessboard, same, reset_path, number
    reset_path = [] #intermediate list required when transferring information from "path" to "same" list

    for i in range(35):
        print("Looking at point [",x,",",y,"]" )
        pos = possible_moves(x,y)
        print("Possibilities:", pos)
        if not pos: #if else condition to dodge an error in the code
            continue
        else:
            mini = pos[0] #takes the first element in the list with all the possible moves
            print("Initial minimum point: ", mini)
            for p in pos: #compares the deg of the first element(vertex) to the deg of all vertices in the list
                if len(possible_moves(p[0],p[1])) < len(possible_moves(mini[0],mini[1])): #if another element has a lower deg, sets mini as that element
                    mini = p
                    print("New minimum point: ", mini)
                elif len(possible_moves(p[0],p[1])) == len(possible_moves(mini[0],mini[1])) and possible_moves(p[0],p[1]) != possible_moves(mini[0], mini[1]):
                    #if two vertices have the same degree, it saves the path with the alternate vertex as one element in the "same" list
                    reset_path = path.copy()
                    reset_path.append(p)
                    same.append(reset_path)
                    reset_path = []
                    print("- Adding", p , "to checkpoint list as deg of", p, "= deg of", mini)
                    print("Same", same)

            x = mini[0]
            y = mini[1]
            path.append([mini[0],mini[1]]) #adds the minimum point to the path list
            print("Path: ", path)
            if chessboard[x][y] == 0: #checks if that vertex has been already visited
                chessboard[x][y] = number #writes the knight move order on that vertex
                number += 1  #sets to 37 at the end of loop
                print("---Next Move---")
                print_chessboard() #calls def print_chessbaord()
            else: #if that vertex is already visited, it breaks the loop
                break
    print("Path: ", path) #prints the entire knight's tour path
def print_chessboard(): #draws the chessboard as a matrix in terminal
    for i in range (6):
        for j in range (6):
            print(chessboard[i][j], end=" ")
        print ("\n")


run = 1
#a system that sets
while run == 1:
    warnsdorffs_rule()
    if path[-1] == [2,1] or path [-1] == [1,2]: #if else condition checks if the path is a closed knight's tour
        run += 1
        #if true break loop
    else:
        #if false,
        print("-----------------redo------------")
        print("same:", same)
        x = same[-1][-1][0]
        y = same[-1][-1][1]
        path = same[-1] #sets the last element in same as the new path
        del same[-1] #deletes that path from the list
        reset_board() #resets the board