import random as rd
import sys
class Input_processor:

    def __init__(self):
        self.charactor = " "

    
    def Input_checker(self):
        try:
            self.charactor = input("Move: ")
            if((self.charactor).upper() in ["A","B","C","D","E","F","G","H","I","J","K"]):
                print("OK")
            else:
                print("Please put the charactor only A-K.")

        except:
            print("Please put the charactor A-K only.")


class Board(Input_processor):

    def __init__(self):
        self.board = [["A","K","C","H"],
                      ["D","E","B","I"],
                      ["J","G","F"," "]]

    def display_board(self):

        b1 = rd.sample(range(3),3)
        b2 = rd.sample(range(4),4)

        for i in range(len(b1)):
            for j in range(len(b2)):
                sys.stdout.write(self.board[b1[i]][b2[j]] + "  ")
            print("\n")

    def check_winner(self):
        if(self.board == [["A","B","C","D"],["E","F","G","H"],["I","J","K"," "]]):
            print("Win!")


if __name__ == '__main__':
    print("Welcome to Sorting Game")
    b = Board()
    i = Input_processor()
    b.display_board()
    i.Input_checker()
    b.check_winner()

