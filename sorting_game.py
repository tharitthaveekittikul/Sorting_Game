import random as rd
import sys
class Board:

    def __init__(self):
        self.board = [["A","B","C","D"],["E","F","G","H"],["I","J","K"," "]]

    def display_board(self):
        b1 = rd.sample(range(3),3)
        b2 = rd.sample(range(4),4)

        for i in range(len(b1)):
            for j in range(len(b2)):
                sys.stdout.write(self.board[b1[i]][b2[j]] + "  ")
            print("\n")

class Input_processor(Board):

    def __init__(self):
        self.charactor = " "

    
    def Input_checker(self):
        self.charactor = input("Move: ")
    


if __name__ == '__main__':
    print("Welcome to Sorting Game")
    b = Board()
    print(b.display_board())