import game
import time


board = game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
while not game.isFinished(board):
    tic = time.perf_counter()
    print("continue game")
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board = game.inputComputer(board)
    toc = time.perf_counter()
    game.printState(board)
    print(f"total time for move took {toc - tic:0.4f} seconds")
print("Game Over:")
