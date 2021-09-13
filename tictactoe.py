import random
import ai

class TicTacToe:
    

    def __init__(self):
        self.winner = "None"
        self.board = []

    def GetValidSpots(self):
        ValidSpots = []
        for i in range(9):
            if(self.board[i] == 0):
                ValidSpots.append(i)
        return ValidSpots
        
    def GetDisplayValue(self, slot):
        if(self.board[slot] == 1):
            return "X"
        elif(self.board[slot] == 4):
            return "O"
        else:
            return "-"

    def HandlePlayerInput(self):
        playerCommandMove = input("Enter your move position: ")

        if playerCommandMove.isdigit():
            playerCommandMove = int(playerCommandMove) - 1
            if playerCommandMove > len(self.board) - 1:
                playerCommandMove = self.GetInputAgain("That value is bigger than the board size! Try another position!: ")

            if playerCommandMove < 0:
                playerCommandMove = self.GetInputAgain("That value is too small! Try another position!: ")

            if (self.board[playerCommandMove] != 0):
                playerCommandMove = self.GetInputAgain("Invalid Position! Try another position!: ")
            return playerCommandMove
        else:
            playerCommandMove = self.GetInputAgain("Ahem that's not even an integer! Try again: ")
        
        


        return playerCommandMove
        
    def GetInputAgain(self, terminalMessage):
        playerCommandMove = input(terminalMessage)

        if playerCommandMove.isdigit():
            playerCommandMove = int(playerCommandMove) - 1
            if playerCommandMove > len(self.board):
                playerCommandMove = self.GetInputAgain("That value is bigger than the board size! Try another position!: ")

            if playerCommandMove < 0:
                playerCommandMove = self.GetInputAgain("That value is too small! Try another position!: ")

            if (self.board[playerCommandMove] != 0):
                playerCommandMove = self.GetInputAgain("Invalid Position! Try another position!: ")
            return playerCommandMove
        else:
            playerCommandMove = self.GetInputAgain("Ahem that's not even an integer! Try again: ")

        return playerCommandMove


    def PlayerMove(self, slot):
        if(self.board[slot] == 0):
            self.board[slot] = 1
            return True
        return False


    def AIMove(self, slot):
        if(self.board[slot] == 0):
            self.board[slot] = 4
            return True
        return False


    def CheckWin(self):
        """
        A better way to check for the win conditions, is to have a list of the 5 potential starting spaces to check.
        Those are positions [0, 1, 2, 3, 6].
        From there check if any neighbors are the same value, and in which direction said neighbor was.
        If there are any neighbors, continue in the same direction to the final value.
        If the final value has the same value as the previous, you know you have found a win condition.
        """

        for i in range(0, 6, 3):
            BoardLineTotal = self.board[i] + self.board[i+1] + self.board[i+2]
            if(BoardLineTotal == 3):
                self.PlayerWin()
                return
            elif(BoardLineTotal == 12):
                self.AIWin()
                return

        for i in range(3):
            BoardLineTotal = self.board[i] + self.board[i+3] + self.board[i+6]
            if(BoardLineTotal == 3):
                self.PlayerWin()
                return
            elif(BoardLineTotal == 12):
                self.AIWin()
                return
        
        BoardLineTotal = self.board[0] + self.board[4] + self.board[8]
        if(BoardLineTotal == 3):
            self.PlayerWin()
            return
        elif(BoardLineTotal == 12):
            self.AIWin()
            return

        BoardLineTotal = self.board[2] + self.board[4] + self.board[6]
        if(BoardLineTotal == 3):
            self.PlayerWin()
            return
        elif(BoardLineTotal == 12):
            self.AIWin()
            return

    def PlayerWin(self):
        print('')
        print('You won!!!')
        print('Here is the final board state:')
        print('==============================')
        self.LogBoard()
        print('==============================')
        self.winner = "Player"


    def AIWin(self):
        print('')
        print('The AI won :<')
        print('Here is the final board state:')
        print('==============================')
        self.LogBoard()
        print('==============================')
        self.winner = "AI"

    def NoneWin(self):
        print('')
        print('Draw.')
        print('Here is the final board state:')
        print('==============================')
        self.LogBoard()
        print('==============================')
        self.winner = "Draw"


    def LogBoard(self):
        print(self.GetDisplayValue(0) + " " + self.GetDisplayValue(1) + " " + self.GetDisplayValue(2))
        print("")
        print(self.GetDisplayValue(3) + " " + self.GetDisplayValue(4) + " " + self.GetDisplayValue(5))
        print("")
        print(self.GetDisplayValue(6) + " " + self.GetDisplayValue(7) + " " + self.GetDisplayValue(8))

 
    def GameTick(self):
        self.LogBoard()

        playerCommandMove = self.HandlePlayerInput()
            
        self.PlayerMove(playerCommandMove)
        self.CheckWin()
        if(len(self.GetValidSpots()) == 0):
            if(self.winner == "None"):
                self.NoneWin()
            return

        if self.winner != "None":
            return

        self.AIMove(self.aiController.ChooseMove(self))

        if(self.winner == "None"):
            self.CheckWin()

    def StartGame(self):
        self.aiController = ai.AIController()
        for i in range(9):
            self.board.append(0)
