import random
import math

class Board:
    def __init__(self):
        """Construct objects of type Board, with the width and height of a checkers board."""
        self.width = 8
        self.height = 8
        self.data = [[' ']*8 for row in range(8)] # set the initial baord empty
        for i in range (3):
            for j in range(8):
                if i%2 == 0:
                    if j%2 == 1:
                        self.data[i][j] = "r"
                if i%2 == 1:
                    if j%2 == 0:
                        self.data[i][j] = "r"
        for i in range(3):
            for j in range(8):
                if i%2 == 1:
                    if j%2 == 1:
                        self.data[7-i][j] = "b"
                if i%2 == 0:
                    if j%2 == 0:
                        self.data[7-i][j] = "b"
    
    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += (str(row)) + ' |'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '  ' + (2*self.width + 1) * '-' + "\n"   # Bottom of the board
        s += '  '
        for i in range(self.width):
            s += (' ' + str(i))
        return s
    def hasJump(self, col, row):
        """
        returns the possible jumps for the piece to make, if any, in a string
        """
        jumps = ''
        if (self.data[row][col] == 'b'):
            if (row - 2 >= 0):
                if (col + 2 <= 7):
                    if ((self.data[row - 1][col + 1] == 'r') or (self.data[row - 1][col + 1] == 'R')):
                        if self.data[row - 2][col + 2] == ' ':
                            jumps += 'bright'
                if (col - 2 >= 0):
                    if ((self.data[row - 1][col - 1] == 'r') or (self.data[row - 1][col - 1] == 'R')):
                        if self.data[row - 2][col - 2] == ' ':
                            jumps += 'blefts'   
        elif (self.data[row][col] == 'r'):
            if (row + 2 <= 7):
                if (col + 2 <= 7):
                    if ((self.data[row + 1][col + 1] == 'b') or (self.data[row + 1][col + 1] == 'B')):
                        if self.data[row + 2][col + 2] == ' ':
                            jumps += 'rlefts'
                if (col - 2 >= 0):
                    if ((self.data[row + 1][col - 1] == 'b') or (self.data[row + 1][col - 1] == 'B')):
                        if self.data[row + 2][col - 2] == ' ':
                            jumps += 'rright'
        elif (self.data[row][col] == 'B'):
            if (row - 2 >= 0):
                if (col + 2 <= 7):
                    if ((self.data[row - 1][col + 1] == 'r') or (self.data[row - 1][col + 1] == 'R')):
                        if self.data[row - 2][col + 2] == ' ':
                            jumps += 'BFrigh'
                if (col - 2 >= 0):
                    if ((self.data[row - 1][col - 1] == 'r') or (self.data[row - 1][col - 1] == 'R')):
                        if self.data[row - 2][col - 2] == ' ':
                            jumps += 'BFleft' 
            if (row + 2 <= 7):
                if (col + 2 <= 7):
                    if ((self.data[row + 1][col + 1] == 'r') or (self.data[row + 1][col + 1] == 'R')):
                        if self.data[row + 2][col + 2] == ' ':
                            jumps += 'BBleft'
                if (col - 2 >= 0):
                    if ((self.data[row + 1][col - 1] == 'r') or (self.data[row + 1][col - 1] == 'R')):
                        if self.data[row + 2][col - 2] == ' ':
                            jumps += 'BBrigh'  
        elif (self.data[row][col] == 'R'):
            if (row - 2 >= 0):
                if (col + 2 <= 7):
                    if ((self.data[row - 1][col + 1] == 'b') or (self.data[row - 1][col + 1] == 'B')):
                        if self.data[row - 2][col + 2] == ' ':
                            jumps += 'RBrigh'
                if (col - 2 >= 0):
                    if ((self.data[row - 1][col - 1] == 'b') or (self.data[row - 1][col - 1] == 'B')):
                        if self.data[row - 2][col - 2] == ' ':
                            jumps += 'RBleft' 
            if (row + 2 <= 7):
                if (col + 2 <= 7):
                    if ((self.data[row + 1][col + 1] == 'b') or (self.data[row + 1][col + 1] == 'B')):
                        if self.data[row + 2][col + 2] == ' ':
                            jumps += 'RFleft'
                if (col - 2 >= 0):
                    if ((self.data[row + 1][col - 1] == 'b') or (self.data[row + 1][col - 1] == 'B')):
                        if self.data[row + 2][col - 2] == ' ':
                            jumps += 'RFrigh'  
        return jumps 
        
    def doJump(self, col, row):
        """
        Performs the jump and checks again if there is another one, does it again until there's no more jump
        """
        direction = self.hasJump(col, row)
        if direction[0] == 'b' or direction[0] == 'r':
            if (direction == 'bright'):
                self.data[row - 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col + 2] = 'b'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif (direction == 'blefts'):
                self.data[row - 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col - 2] = 'b'
                #print(self)
                if self.hasJump(col - 2, row - 2) != '':    
                    self.doJump(row - 2, col - 2)
            elif (direction == 'rlefts'):
                self.data[row + 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col + 2] = 'r'
                #print(self)
                if self.hasJump(col + 2, row + 2) != '':
                    self.doJump(row + 2, col + 2)
            elif (direction == 'rright'):
                self.data[row + 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col - 2] = 'r'
                #print(self)
                if self.hasJump(col - 2, row + 2) != '':
                    self.doJump(row + 2, col - 2)
        elif len(direction) == 6 and (direction[0] == 'B' or direction[0] == 'R'):
            if direction[0:6] == 'BFrigh':
                self.data[row - 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col + 2] = 'B'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif direction[0:6] == 'BFleft':
                self.data[row - 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col - 2] = 'B'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif direction[0:6] == 'BBleft':
                self.data[row + 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col + 2] = 'B'
                #print(self)
                if self.hasJump(col + 2, row + 2) != '':
                    self.doJump(row + 2, col + 2)
            elif direction[0:6] == 'BBrigh':
                self.data[row + 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col - 2] = 'B'
                #print(self)
                if self.hasJump(col - 2, row + 2) != '':
                    self.doJump(row + 2, col - 2)
            elif direction[0:6] == 'RBrigh':
                self.data[row - 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col + 2] = 'R'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif direction[0:6] == 'RBleft':
                self.data[row - 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col - 2] = 'R'
                #print(self)
                if self.hasJump(col - 2, row - 2) != '':
                    self.doJump(row - 2, col - 2)
            elif direction[0:6] == 'RFleft':
                self.data[row + 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col + 2] = 'R'
                #print(self)
                if self.hasJump(col + 2, row + 2) != '':
                    self.doJump(row + 2, col + 2)
            elif direction[0:6] == 'RFrigh':
                self.data[row + 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col - 2] = 'r'
                #print(self)
                if self.hasJump(col - 2, row + 2) != '':
                    self.doJump(row + 2, col - 2)
        elif len(direction) > 6 and (direction[0] == 'B' or direction[0] == 'R'):
            choice1 = direction[0:6]
            choice2 = direction[6:]

            if choice1 == 'BFrigh':
                print('A possible jump is forward right')
            elif choice1 == 'BFleft':
                print('A possible jump is forward left')
            elif choice1 == 'BBleft':
                print('A possible jump is back left')
            elif choice1 == 'BBrigh':
                print('A possible jump is back right')
            elif choice1 == 'RBrigh':
                print('A possible jump is back right')
            elif choice1 == 'RBleft':
                print('A possible jump is back left')
            elif choice1 == 'RFleft':
                print('A possible jump is forward left')
            elif choice1 == 'RFrigh':
                print('A possible jump is forward right')

            if choice2 == 'BFrigh':
                print('A possible jump is forward right')
            elif choice2 == 'BFleft':
                print('A possible jump is forward left')
            elif choice2 == 'BBleft':
                print('A possible jump is back left')
            elif choice2 == 'BBrigh':
                print('A possible jump is back right')
            elif choice2 == 'RBrigh':
                print('A possible jump is back right')
            elif choice2 == 'RBleft':
                print('A possible jump is back left')
            elif choice2 == 'RFleft':
                print('A possible jump is forward left')
            elif choice2 == 'RFrigh':
                print('A possible jump is forward right')

            current_choice = str(input("Choose which choice of direction to move (1/2): "))
            if current_choice == 1:
                current_choice = choice1
            elif current_choice == 2:
                current_choice = choice2
            else:
                print("Please enter a valid input of 1 or 2")

            if current_choice == 'BFrigh':
                self.data[row - 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col + 2] = 'B'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif current_choice == 'BFleft':
                self.data[row - 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col - 2] = 'B'
                #print(self)
                if self.hasJump(col - 2, row - 2) != '':
                    self.doJump(row - 2, col - 2)
            elif current_choice == 'BBleft':
                self.data[row + 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col + 2] = 'B'
                #print(self)
                if self.hasJump(col + 2, row + 2) != '':
                    self.doJump(row + 2, col + 2)
            elif current_choice == 'BBrigh':
                self.data[row + 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col - 2] = 'B'
                #print(self)
                if self.hasJump(col - 2, row + 2) != '':
                    self.doJump(row + 2, col - 2)
            elif current_choice == 'RBrigh':
                self.data[row - 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col + 2] = 'R'
                #print(self)
                if self.hasJump(col + 2, row - 2) != '':
                    self.doJump(row - 2, col + 2)
            elif current_choice == 'RBleft':
                self.data[row - 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row - 2][col - 2] = 'R'
                #print(self)
                if self.hasJump(col - 2, row - 2) != '':
                    self.doJump(row - 2, col - 2)
            elif current_choice == 'RFleft':
                self.data[row + 1][col + 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col + 2] = 'R'
                #print(self)
                if self.hasJump(col + 2, row + 2) != '':
                    self.doJump(row + 2, col + 2)
            elif current_choice == 'RFrigh':
                self.data[row + 1][col - 1] = ' '
                self.data[row][col] = ' '
                self.data[row + 2][col - 2] = 'r'
                #print(self)
                if self.hasJump(col - 2, row + 2) != '':
                    self.doJump(row + 2, col - 2)


    def hasEmptyMove(self,col,row,nCol,nRow,br):
        if nCol not in range(0,8):
            return False
        if nRow not in range(0,8):
            return False
        if br == 'b':
            if self.data[nRow][nCol] == ' ':
                if (row-nRow == 1 and abs(nCol-col) == 1):
                    return True
        if br == 'r':
            if self.data[nRow][nCol] == ' ':
                if (nRow-row == 1 and abs(nCol-col) == 1):
                    return True
        if br == 'B' or 'R':
            if self.data[nRow][nCol] == ' ':
                if abs(row-nRow) == 1 and abs(col-nCol) == 1:
                    return True
        return False
    
    def makeKing(self,col,row):
        if self.data[row][col] == 'b' and row == 0:
            self.data[row][col] = 'B'
        if self.data[row][col] == 'r' and row == 7:
            self.data[row][col] = 'R'
    
    def move(self,col,row,nCol,nRow,br): 
        """
        advances the game by one turn.
        """
        if self.hasEmptyMove(col,row,nCol,nRow,br) == True:
            self.data[row][col] = ' '
            self.data[nRow][nCol] = br
        #print(self)
    
    def resetBoard(self):
        b = Board()
        return b
    
    def canMove(self,br):
        if br = 'r':
            for i in range(self.width):
                    for j in range(self.height):
                        if self[i][j] == 'r' or 'R':
                            counter += 1
                            if self.hasEmptyMove(i,j,i+1,j+1,'r') == True: return True
                            if self.hasEmptyMove(i,j,i-1,j+1,'r') == True: return True
        if br == 'b':
            for i in range(self.width):
                for j in range(self.height):
                    if self[i][j] == 'b' or 'B':
                        counter += 1
                        if self.hasEmptyMove(i,j,i+1,j-1,'b') == True: return True
                        if self.hasEmptyMove(i,j,i-1,j-1,'b') == True: return True
    def endGame(self,br):
        """
        Determines if a player has won.
        The Game ends if a player has no possible moves, or if he has no more pieces on the board
        """
        if br == 'r':
            if self.count('r' or 'R') == 0: return True
            if self.canMove(br):
                return False
        if br == 'b':
            if self.count('b' or 'B') == 0: return True
            if self.canMove(br):
                return False
        return False
    
    def hostGame(self):
        """
        Runs a game of checkers, with the option to play against an AI
        """
        print("Would you like to play against AI? (Y/N)")
        t = str(input())
        x = 1
        rb = 'b'
        redBlack = 'Red'
        print("*When entering jumps, still enter where to move as the next row or where the enemy piece is, not the open space*")
        if t == 'Y':
            while(x < 10000):
                print(self)
                print("Your turn:")
                current_piece = str(input("Choose a piece to move (col row): "))
                move_to = str(input("Choose where to move (col row): "))
                col = int(current_piece[0])
                row = int(current_piece[2])
                toCol = int(move_to[0])
                toRow = int(move_to[2])
                if self.hasJump(col,row) != '':
                    self.doJump(col,row)
                else:
                    while self.hasEmptyMove(col,row,toCol,toRow,rb) == False:
                        print("That's an illegal move, enter another move:")
                        current_piece = str(input("Choose a new piece to move (col row): "))
                        move_to = str(input("Choose a new place to move to (col row): "))
                    self.move(col,row,toCol,toRow,rb)
                self.makeKing(toCol, toRow)
                self.moveAI()
                x+=1
        #print(self)
        while(x < 10000):
            if x % 2 == 1:
                rb = 'b'
                redBlack = 'Black'
            else: 
                rb = 'r'
                redBlack = "Red"
            print(redBlack,"'s move!")
            current_piece = str(input("Choose a piece to move (col row): "))
            move_to = str(input("Choose where to move (col row): "))
            col = int(current_piece[0])
            row = int(current_piece[1])
            toCol = int(move_to[0])
            toRow = int(move_to[1])
            if self.hasJump(col,row) != '':
                self.doJump(col,row)
            else:
                while self.hasEmptyMove(col,row,toCol,toRow,rb) == False:
                    print("That's an illegal move, enter another move:")
                    current_piece = str(input("Choose a new piece to move (col row): "))
                    move_to = str(input("Choose a new place to move to (col row): "))
                self.move(col,row,toCol,toRow,rb)
            x += 1

    def anyEmptyMove(self, col, row):
        t = False
        if self.hasEmptyMove(col, row, col + 1, row + 1, 'r'):
            t = True
        if self.hasEmptyMove(col, row, col - 1, row + 1, 'r'):
            t = True
        return t
    
    def moveAI(self):
        """
        Jumps if you can, otherwise moves the piece it can closest to the other side of the board
        """
        counter = 0
        for i in range(8):
            for j in range(8):
                if self.data[i][j] == 'r':
                    counter += 1
                    if self.hasJump(j, i):
                        self.doJump(j, i)
                        self.makeKing(j, i)
                        return
        temp = 0
        max = 0
        bool = False
        for a in range(8):
            for b in range(8):
                if self.data[a][b] == 'r':
                    if self.anyEmptyMove(b, a):
                        if a > max:
                            max = a
                            temp = b
        
        if self.hasEmptyMove(temp, max, temp + 1, max + 1, 'r'):
            self.move(temp,max,temp+1,max+1,'r')
            self.makeKing(j, i)
            #print(self)
            bool = True
            return
        elif self.hasEmptyMove(temp, max, temp + 1, max - 1, 'r'):
            self.move(temp,max,temp+1,max-1,'r')
            self.makeKing(j, i)
            #print(self)
            bool = True
            return



    
