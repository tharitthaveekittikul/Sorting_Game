import random as rd
import sys
class Input_processor:

    def __init__(self):
        self.charactor = " "

    def Input_checker(self):
        while True:
            try:
                self.charactor = input("Move: ").upper()
                if((self.charactor) in ["A","B","C","D","E","F","G","H","I","J","K"]):
                    break
                else:
                    print("Please put the charactor only A-K.")

            except:
                print("Please put the charactor A-K only.")
    
    def get_charactor(self):
        return self.charactor


class Board:

    def __init__(self):
        
        self.charactor_list = ["A","B","C","D","E","F","G","H","I","J","K"," "]
        self.cha_rd = rd.sample(self.charactor_list,12)
        self.board = [["A","B","C","D"],
                      ["E","F","G","H"],
                      ["I","J","K"," "]] # main board
        

    def random_board(self):
        for i in range(3):
            for j in range(4):
                self.board[i][j] = self.cha_rd[j-3]
                self.cha_rd.remove(self.board[i][j])

    def get_board(self):
        return self.board

    def display_board(self):
        self.get_board()
        for i in range(3):
            for j in range(4):
                sys.stdout.write(self.board[i][j] + "  ")
            print("\n")

    def check_winner(self):
        if(self.board == [["A","B","C","D"],["E","F","G","H"],["I","J","K"," "]]):
            return True
if __name__ == '__main__':
    print("Welcome to Sorting Game")
    b = Board()
    b.display_board()
    b.check_winner()