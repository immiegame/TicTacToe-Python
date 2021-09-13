import random

class AIController:

    def __init__(self):

        """
        0 - 2
        0, 3, 6
        0, 4, 8
        1, 4, 7
        2, 5, 8
        3, 4, 5
        6, 7, 8
        6, 4, 2
        """

        size = 3

        self.lines = []

        self.lines.append(range(0, size))
        self.lines.append(range(0, size * size + size, 4))
        self.lines.append(range(0, size * size, 3))

        self.lines.append(range(1, size * size + 1, 3))
        self.lines.append(range(2, size * size + 2, 3))

        self.lines.append(range(size, size * 2))
        self.lines.append(range(size * 2, size * size))

        self.lines.append(range(size * 2, 0, -2))


    def GetPossiblePlayerWin(self, board):
        self.playerWinConditions = []
        for i in range(len(self.lines)):
            iterSum = 0
            for j in self.lines[i]:
                iterSum += board[j]
            if iterSum is 2:
                #print('oho check ' + str(iterSum) + ' at line index ' + str(i))

                for k in self.lines[i]:
                    if board[k] is 0:
                        self.playerWinConditions.append(k)
                        break

        #print(self.playerWinConditions)

    def GetPossibleAIWin(self, board):
        self.AIWinConditions = []
        for i in range(len(self.lines)):
            iterSum = 0
            for j in self.lines[i]:
                iterSum += board[j]
            if iterSum is 8:
                #print('oho check ' + str(iterSum) + ' at line index ' + str(i))

                for k in self.lines[i]:
                    if board[k] is 0:
                        self.AIWinConditions.append(k)
                        break

    def ChooseMove(self, boardInstance):
        choices = boardInstance.GetValidSpots()
        setChoices = set(choices)
        
        """
        This gives increased chances of choosing to use the corners
        Furthermore, by making it into a set for the lookup, in the event of expanding the system
        to use larger boards, finding if the list contains the element won't be too expensive
        """
        
        if 0 in setChoices:
            choices.append(0)
        if 2 in setChoices:
            choices.append(2)
        if 6 in setChoices:
            choices.append(6)
        if 8 in setChoices:
            choices.append(8)

        choice = random.choice(choices)
        
        self.GetPossibleAIWin(boardInstance.board)
        if(len(self.AIWinConditions) > 0):
            print('AI: I WIN!!!')
            choice = random.choice(self.AIWinConditions)
            return choice


        self.GetPossiblePlayerWin(boardInstance.board)
        if(len(self.playerWinConditions) > 0):
            if(len(self.playerWinConditions) > 1):
                print('AI: Uh oh...')
            else:
                print("AI: Yeah I see that win condition you're trying to do")
            choice = random.choice(self.playerWinConditions)

        return choice