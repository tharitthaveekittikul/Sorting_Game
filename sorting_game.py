import random as rd
import sys
class Input_processor:

    def __init__(self):
        self.charactor = " "

    
    def Input_checker(self):
        while True:
            try:
                self.charactor = input("Move: ")
                if((self.charactor).upper() in ["A","B","C","D","E","F","G","H","I","J","K"]):
                    # print("OK")
                    break
                else:
                    print("Please put the charactor only A-K.")

            except:
                print("Please put the charactor A-K only.")


class Board(Input_processor):

    def __init__(self):
        self.board = [["A","B","C","D"],
                      ["E","F","G","H"],
                      ["I","J","K"," "]] # main board

    def display_board(self):

        charactor_list = ["A","B","C","D","E","F","G","H","I","J","K"," "]
        cha_rd = rd.sample(charactor_list,12)
        # print(cha_rd)
        for i in range(3):
            for j in range(4):
                self.board[i][j] = cha_rd[j-3]
                cha_rd.remove(self.board[i][j])
                sys.stdout.write(self.board[i][j] + "  ")
            print("\n")
               


    def check_winner(self):
        if(self.board == [["A","B","C","D"],["E","F","G","H"],["I","J","K"," "]]):
            print("Win!")

    def change_position(self):
        i = Input_processor()
        i.Input_checker()


if __name__ == '__main__':
    print("Welcome to Sorting Game")
    b = Board()
    b.display_board()
    b.change_position()
    b.check_winner()

