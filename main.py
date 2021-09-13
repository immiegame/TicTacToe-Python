from tictactoe import TicTacToe

def DoGameLoop():
    Game = TicTacToe()
    Game.StartGame()
    print("YOU ARE X!!")
    print("===========")
    while(Game.winner == "None"):
        Game.GameTick()

    keepPlaying = input("Would you like to play again? y / n :")
    if keepPlaying == 'y':
        print("STARTING AGAIN")
        print()
        DoGameLoop()
    elif keepPlaying == 'n':
        print('Thank you for playing! :)')
    else:
        print("I don't understand what you just said but thank you for playing! :)")


if __name__ == "__main__":
    DoGameLoop()