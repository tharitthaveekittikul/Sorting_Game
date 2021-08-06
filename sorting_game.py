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

    def change_position(self):
        while (True):
            I = Input_processor()     
            I.Input_checker()
            gb = self.get_board()

            for i in range(3):
                for j in range(4):
                    if(gb[i][j] == I.get_charactor()):
                        index_char = [i,j]

            # change 2 position
            if(index_char == [0,0]):
                if(gb[0][1] == " "):
                    gb[0][0],gb[0][1] = gb[0][1],gb[0][0]
                    break

                elif(gb[1][0] == " " ):
                    gb[0][0],gb[1][0] = gb[1][0],gb[0][0]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [0,3]):
                if(gb[0][2] == " "):
                    gb[0][3],gb[0][2] = gb[0][2],gb[0][3]
                    break

                elif(gb[1][3] == " "):
                    gb[0][3],gb[1][3] = gb[1][3],gb[0][3]
                    break

                else:
                    print("Cannot Change try again.")
            
            elif(index_char == [2,0]):
                if(gb[1][0] == " "):
                    gb[2][0],gb[1][0] = gb[1][0],gb[2][0]
                    break
                    
                elif(gb[2][1] == " "):
                    gb[2][0],gb[2][1] = gb[2][1],gb[2][0]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [2,3]):
                if(gb[1][3] == " "):
                    gb[2][3],gb[1][3] = gb[1][3],gb[2][3]
                    break
                    
                elif(gb[2][2] == " "):
                    gb[2][3],gb[2][2] = gb[2][2],gb[2][3]
                    break

                else:
                    print("Cannot Change try again.")

            # change 3 position
            elif(index_char == [0,1]):
                if(gb[0][0] == " "):
                    gb[0][1],gb[0][0] = gb[0][0],gb[0][1]
                    break
                    
                elif(gb[1][1] == " "):
                    gb[0][1],gb[1][1] = gb[1][1],gb[0][1]
                    break

                elif(gb[0][2] == " "):
                    gb[0][1],gb[0][2] = gb[0][2],gb[0][1]
                    break

                else:
                    print("Cannot Change try again.")
            
            elif(index_char == [0,2]):
                if(gb[0][3] == " "):
                    gb[0][2],gb[0][3] = gb[0][3],gb[0][2]
                    break
                    
                elif(gb[0][1] == " "):
                    gb[0][2],gb[0][1] = gb[0][1],gb[0][2]
                    break

                elif(gb[1][2] == " "):
                    gb[0][2],gb[1][2] = gb[1][2],gb[0][2]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [1,0]):
                if(gb[1][1] == " "):
                    gb[1][0],gb[1][1] = gb[1][1],gb[1][0]
                    break
                    
                elif(gb[0][0] == " "):
                    gb[1][0],gb[0][0] = gb[0][0],gb[1][0]
                    break

                elif(gb[2][0] == " "):
                    gb[1][0],gb[2][0] = gb[2][0],gb[1][0]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [1,3]):
                if(gb[0][3] == " "):
                    gb[1][3],gb[0][3] = gb[0][3],gb[1][3]
                    break
                    
                elif(gb[1][2] == " "):
                    gb[1][3],gb[1][2] = gb[1][2],gb[1][3]
                    break

                elif(gb[2][3] == " "):
                    gb[1][3],gb[2][3] = gb[2][3],gb[1][3]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [2,1]):
                if(gb[1][1] == " "):
                    gb[2][1],gb[1][1] = gb[1][1],gb[2][1]
                    break
                    
                elif(gb[2][0] == " "):
                    gb[2][1],gb[2][0] = gb[2][0],gb[2][1]
                    break

                elif(gb[2][2] == " "):
                    gb[2][1],gb[2][2] = gb[2][2],gb[2][1] 
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [2,2]):
                if(gb[1][2] == " "):
                    gb[2][2],gb[1][2] = gb[1][2],gb[2][2]
                    break
                    
                elif(gb[2][1] == " "):
                    gb[2][2],gb[2][1] = gb[2][1],gb[2][2]
                    break

                elif(gb[2][3] == " "):
                    gb[2][2],gb[2][3] = gb[2][3],gb[2][2]
                    break

                else:
                    print("Cannot Change try again.")

            # Change 4 position

            elif(index_char == [1,1]):
                if(gb[0][1] == " "):
                    gb[1][1],gb[0][1] = gb[0][1],gb[1][1]
                    break
                    
                elif(gb[1][0] == " "):
                    gb[1][1],gb[1][0] = gb[1][0],gb[1][1]
                    break

                elif(gb[2][1] == " "):
                    gb[1][1],gb[2][1] = gb[2][1],gb[1][1]
                    break
                
                elif(gb[1][2] == " "):
                    gb[1][1],gb[1][2] = gb[1][2],gb[1][1]
                    break

                else:
                    print("Cannot Change try again.")

            elif(index_char == [1,2]):
                if(gb[0][2] == " "):
                    gb[1][2],gb[0][2] = gb[0][2],gb[1][2]
                    break
                    
                elif(gb[1][1] == " "):
                    gb[1][2],gb[1][1] = gb[1][1],gb[1][2]
                    break

                elif(gb[2][2] == " "):
                    gb[1][2],gb[2][2] = gb[2][2],gb[1][2]
                    break
                
                elif(gb[1][3] == " "):
                    gb[1][2],gb[1][3] = gb[1][3],gb[1][2]
                    break

                else:
                    print("Cannot Change try again.")
        
if __name__ == '__main__':
    print("Welcome to Sorting Game")
    b = Board()
    b.random_board()
    while(True):
        b.display_board()
        b.change_position()
        if (b.check_winner() == True):
            b.display_board()
            print("Win!!")
            break