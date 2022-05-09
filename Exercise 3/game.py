import copy
from typing import Sized
import alphaBetaPruning
import random
import numpy as np

VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board


ROWS = 6
COLUMNS = 7


class game:
    board = []
    size = ROWS * COLUMNS
    playTurn = HUMAN

    # Used by alpha-beta pruning to allow pruning

    """
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of intgers. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    """


def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(ROWS):
        s.board = s.board + [COLUMNS * [0]]

    s.playTurn = HUMAN
    s.size = ROWS * COLUMNS
    s.val = 0.00001

    # return [board, 0.00001, playTurn, r*c]     # 0 is TIE


def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    print("board ", s2.board)
    return s2


def value(s):
    # Returns the heuristic value of s

    # check for tie if there is no more room on the board
    if any(0 in it for it in s.board):
        # get who piece it is now
        piece = COMPUTER
        if s.playTurn == HUMAN:
            piece = HUMAN

        # this part of the code check for winning moves so that the computer can block the move that would make
        # a 4 in a row

        # check for victory if the Human won
        if winning_move(s.board, HUMAN, SIZE):

            # human won so return the smallest number and vise versa for the computer
            if s.playTurn == HUMAN:
                return VICTORY
            else:
                return LOSS
        elif winning_move(s.board, COMPUTER, SIZE):
            # computer won so return the largest number and vise versa for the computer
            if s.playTurn == COMPUTER:
                return LOSS
            else:
                return VICTORY
        # get value of board
        else:
            # get the score of the board
            score = score_position(s.board)
            # if the score is zero that means there is no pieces on the board so pick a random sport
            if score == 0:
                # computer won so return the largest number and vise versa for the computer
                if s.playTurn == COMPUTER:
                    return -0.5
                else:
                    return 0.5
            else:
                return score
    else:
        # return if there is a tie
        return TIE


def score_position(board):

    """
    The value of each line is the sum of the values of its 4
    individual squares, and the value of the board is the sum of
    the values of the 69 potential winning lines. In other words,
    each square is weighted according to the number of unique winning
    lines it can be a member of, illustrated by the following
    """
    bit_map = [
        [3, 4, 5, 7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5],
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3],
    ]

    """
    We will calculate the score base on where the tiles are located. we will take the negative summation of all the players pieces
    and take the positive summation of the AI pieces. Return the total and that is the score of the board.  
    """
    total_score = 0
    for x in range(ROWS):
        for y in range(COLUMNS):
            if board[x][y] == HUMAN:
                total_score -= bit_map[x][y]
            elif board[x][y] == COMPUTER:
                total_score += bit_map[x][y]
            else:
                pass

    return total_score


def winning_move(board, piece, size=SIZE):

    # check vertical spaces
    for y in range(COLUMNS):
        for x in range(ROWS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    # check horizontal spaces
    for x in range(ROWS):
        for y in range(COLUMNS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x][y + i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True

    # check / diagonal spaces
    for x in range(ROWS - (size - 1)):
        for y in range((size - 1), COLUMNS):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y - i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    # check \ diagonal spaces
    for x in range(ROWS - (size - 1)):
        for y in range(COLUMNS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y + i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    return False


def block_move(board, piece, size=SIZE):

    size = size - 1
    # check vertical spaces
    for y in range(COLUMNS):
        for x in range(ROWS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    # check horizontal spaces
    for x in range(ROWS):
        for y in range(COLUMNS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x][y + i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True

    # check / diagonal spaces
    for x in range(ROWS - (size - 1)):
        for y in range((size - 1), COLUMNS):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y - i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    # check \ diagonal spaces
    for x in range(ROWS - (size - 1)):
        for y in range(COLUMNS - (size - 1)):
            check = np.zeros(size)
            for i in range(size):
                if board[x + i][y + i] == piece:
                    check[i] = 1
            if 0 not in check:
                return True
    return False


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.
    for r in range(ROWS):
        print("\n|", end="")
        # print("\n",len(s[0][0])*" --","\n|",sep="", end="")
        for c in range(COLUMNS):
            if s.board[r][c] == COMPUTER:
                print("X|", end="")
            elif s.board[r][c] == HUMAN:
                print("O|", end="")
            else:
                print(" |", end="")

    print()

    for i in range(COLUMNS):
        print(" ", i, sep="", end="")

    print()
    if any((1 or 5) in it for it in s.board):
        val = value(s)

        if val == VICTORY:
            print("I won!")
        elif val == LOSS:
            print("You beat me!")
        elif val == TIE:
            print("It's a TIE")


def isFinished(s):
    # Seturns True iff the game ended
    return value(s) in [LOSS, VICTORY, TIE] or s.size == 0


def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s.playTurn == HUMAN


def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN

    return s.playTurn


def makeMove(s, c):
    # Puts mark (for human. or computer.) in col. c
    # and switches turns.
    # Assumes the move is legal.

    r = 0
    while r < ROWS and s.board[r][c] == 0:
        r += 1

    s.board[r - 1][c] = s.playTurn  # marks the board
    s.size -= 1  # one less empty cell
    if s.playTurn == COMPUTER:
        s.playTurn = HUMAN
    else:
        s.playTurn = COMPUTER


def inputMove(s):
    # Reads, enforces legality and executes the user's move.

    # self.printState()
    flag = True
    while flag:
        c = int(input("Enter your next move: "))
        if c < 0 or c >= COLUMNS or s.board[0][c] != 0:
            print("Illegal move.")

        else:
            flag = False
            makeMove(s, c)


def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(COLUMNS)):
        print("c=", c)
        if s.board[0][c] == 0:
            print("possible move ", c)
            tmp = cpy(s)
            makeMove(tmp, c)
            print("tmp board=", tmp.board)
            ns += [tmp]
            print("ns=", ns)
    print("returns ns ", ns)
    return ns


def inputComputer(s):
    return alphaBetaPruning.go(s)
