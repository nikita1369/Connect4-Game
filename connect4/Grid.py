from connect.Player import Player


class Grid:
    def __init__(self, player1, player2, matrix):
        self.player1 = player1
        self.player2 = player2
        self.matrix = matrix

    def addMove(self, column, player):  # Add's a move if valid
        row = 1

        if self.inRange(column):  # First check if the column is in range ( 1 - 7)
            row = len(self.matrix[column]) - 1  # If it is, then get the number of rows to check
        else:
            notInRange = True  # If not in range,
            while notInRange:  # Loop Until Player
                column = int(input("RANGE MUST BE BETWEEN 1 - 7: ")) - 1
                if self.inRange(column):  # Enters a Valid Range
                    row = len(self.matrix[column]) - 1
                    notInRange = False

        notFull = False
        if self.inRange(column):
            notFull, row, column = self.columnNotFull(column)  # checks if a column is full or not
        else:
            notInRange = True
            while notInRange:
                column = int(input(player.name + " input range 1-7: ")) - 1
                if self.inRange(column):
                    notFull, row, column = self.columnNotFull(column)  # checks if a column is full or not
                    notInRange = False

        if notFull:
            self.matrix[column][row] = player.color  # if Not FUll (ADD TO COLUMN)
            if self.checkVertical(player, column, row) or self.checkHorizontal(player, column,
                                                                               row) or self.checkDiagonals(player,
                                                                                                           column, row):
                return False, player, row  # returning false will end the loop because player won
            else:
                return True, None, row  # returning true will let the game run
        else:
            # COMMENTED THIS OUT BECAUSE WHILE LOOP CAUSES GUI TO CRASH
            # IN GUI -> IF THE ROW IS 0 I REMOVE THE TRIANGLE BUTTON SO USERS CANNOT CLICK A FILLED ROW, SO NO VALIDATION NEEDED HERE
            notValidEntry = True  # if column is full

    #             while notValidEntry:
    #                 column = input(player.name + " choose a column that is not full: ") - 1
    #                 validEntry, row, column = self.columnNotFull(column)  # continue to ask until user
    #
    #                 if validEntry:                  #enters a valid column (COLUMN THAT IS NOT FULL)
    #                     self.matrix[column][row] = player.color
    #                     if self.checkVertical(player, column, row) or self.checkHorizontal(player, column, row) or self.checkDiagonals(player, column, row):     # if Not FULL (ADD TO COLUMN)
    #                         return False, player, row    # returning false will end the game
    #                     else:
    #                         return True, None, row    # returning true will let the game run
    #                     notValidEntry = False

    # I DO NOT USE THIS METHOD BECAUSE I TAKE USER INPUT THROUGH TRIANGLE BUTTON CLICK
    def whosTurn(self, player1, player2):  # checks whos turn it is
        if player1.state == True:
            col = input("Which Column Player 1?")
            return (int(col) - 1), player1, player2
        else:
            col = input("Which Column Player 2?")
            return (int(col) - 1), player2, player1

    def columnNotFull(self, column):  # Checks if a given column is full
        if self.inRange(column):  # Checks if column is in range
            row = len(self.matrix[column]) - 1
            while (self.matrix[column][row] != 1 or self.matrix[column][row]) != 2 and row >= 0:
                if self.matrix[column][row] == 0:
                    return (True, row, column)  # Loop to find a row to put the players move
                row -= 1
        else:  # If not in range
            notInRange = True
            while notInRange:  # Loop  to find a valid column
                column = input("Input range 1-7: ") - 1

                if self.inRange(column):  # that is in range

                    row = len(self.matrix[column]) - 1
                    while (self.matrix[column][row] != 1 or self.matrix[column][row]) != 2 and row >= 0:
                        print(self.matrix[column][row])
                        if self.matrix[column][row] == 0:
                            return (True, row, column)  # and that is not full
                        row -= 1
                    notInRange = False

        return (False, -1, column)

    def inRange(self, column):
        if column <= 6 and column >= 0:  # simply checks if the column is in range
            return True  # (1 - 7)
        return False

    def rowInRange(self, row):
        if row <= 5 and row >= 0:
            return True
        return False

    def checkVertical(self, player, column, row):  # checks vertical for a win
        match = 0  # initalize number of matches to 0

        for checkUp in range(row, 6, 1):
            if self.matrix[column][checkUp] == player.color:
                match += 1  # incement matches by one if match found
            if match == 4:  # if 4 consecutive matches, That player wins
                print("VERTICAL WIN")
                player.wins += 1    # increment the number of wins of that player
                return True
            else:  # if not a consecutive match, then not a win
                if self.matrix[column][checkUp] != player.color:
                    return False
        print("returning false")
        return False

    def checkHorizontal(self, player, column, row):  # checks horizontal for a win

        match = 0
        for checkUp in range(column, (column - 4), -1):  # FIRST LOOP checks to the right
            if self.inRange(checkUp):
                if self.matrix[checkUp][row] == player.color:
                    match += 1
                if match == 4:  # if 4 matches found, return True for win
                    print("HORIZONTAL WIN")
                    player.wins += 1  # increment the number of wins of that player
                    return True
                if self.matrix[checkUp][row] != player.color or checkUp == -1:  # stops loop when no match is reached
                    break
            else:
                break

        for checkUp in range((column + 1), (column + 4)):  # SECOND LOOP
            if self.inRange(checkUp):
                if self.matrix[checkUp][row] == player.color:  # checks to the left
                    match += 1
                if match == 4:  # if the combined matches from the left add up to 4
                    print("HORIZONTAL WIN")
                    player.wins += 1  # increment the number of wins of that player
                    return True  # return True for win
                if self.matrix[checkUp][row] != player.color:
                    break  # if no match, and match < 4, stop searching
            else:
                return False
        return False

    def checkDiagonals(self, player, column, row):
        # initialize match to 0
        match = 0

        for checkUp in range(4):  # first Two loops check one diagonal
            # LOOP ONE CHECKS (FROM slot to upper left)
            if self.inRange(column + checkUp) and self.rowInRange(row - checkUp):
                if self.matrix[column + checkUp][row - checkUp] == player.color:
                    match += 1  # if match, increment
                    if match == 4:  # if 4 matches, return true for the win
                        player.wins += 1  # increment the number of wins of that player
                        return True
                else:
                    break  # break loop because no match to player
            else:
                break  # break because out of range

        for checkDown in range(3):  # LOOP TWO IS A CONTINUATION OF THE FIRST DIAGONAL
            # (from slot to lower right)
            if self.inRange(column - checkDown - 1) and self.rowInRange(row + checkDown + 1):
                if self.matrix[column - checkDown - 1][row + checkDown + 1] == player.color:
                    match += 1
                    if match == 4:
                        player.wins += 1
                        return True
                else:
                    break  # break because no match
            else:
                break  # break because not in range

        # reset match to 0 because no first diagonal was not a win, checking for other diagonal
        match = 0

        # First loop of second diagonal will check from (slot to upper right)

        for checkUp in range(4):
            if self.inRange(column - checkUp) and self.rowInRange(row - checkUp):
                if self.matrix[column - checkUp][row - checkUp] == player.color:
                    match += 1
                    if match == 4:
                        player.wins += 1
                        return True
                else:
                    break  # break because not match
            else:
                break  # break because out of range

        # Second loop of second diagonal will check (slot + 1 to lower left)

        for checkDown in range(3):
            if self.inRange(column + checkDown + 1) and self.rowInRange(row + checkDown + 1):
                if self.matrix[column + checkDown + 1][row + checkDown + 1] == player.color:
                    match += 1
                    if match == 4:
                        player.wins += 1
                        return True  # Return true for the win
                else:
                    break  # break because no longer a match
            else:
                break  # break because out of range
        return False

    def checkForDraw(self):
        print("CHECKING FOR A DRAW")
        for row in self.matrix:
            for slot in row:
                if slot == 0:
                    return False  # returning false means no draw
        return True  # returning true results in a draw

    def printGame(self):
        for row in self.matrix:
            print(row)