# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:01:01 2018

@author: frederick-PC @SirToh
"""

import os

class TicTacPy():
    board = ["1","2","3","4","5","6","7","8","9"]
    play_ = True
    player1 = ""
    player2 = ""
    def __init__(self):
        while True:
            self.Header()
            print ()
            self.player1 = input("Player X - enter name : ")
            self.player2 = input("Player O - enter name : ")
            
            os.system("cls")
            self.Header()
            print ("{} vs {}\nLet's Play".format(self.player1,self.player2))
            
            play = input("Type quit to exit\nPress enter to continue . . . ")
            if play != "quit":
                os.system("cls")
                self.Header()
                self.ResetBoard()
                self.PrintBoard()    
                self.PlayGame()
                input()
                break
            else:
               break
        
    def Header(self):
        print ("|" *45)
        print ("  TICTACPY  ".center(45,"|"))
        print ("|" *45)
        
    def ResetBoard(self):
        self.board = ["1","2","3","4","5","6","7","8","9"]
    
    def PrintBoard(self):
        print("""
         {} | {} | {} 
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
        """.format(self.board[0],self.board[1],self.board[2],\
                    self.board[3],self.board[4],self.board[5],\
                    self.board[6],self.board[7],self.board[8]))
    
    def GetTurn(self, char_, pos_):
        self.board[pos_ - 1] = char_

    def IsBoardComplete(self):
        ctr = 0;
        for i in self.board:
            if i == "X" or i == "O":
                ctr += 1
        
        if ctr == 9:
            return True
        else:
            return False
        print(ctr)
        
    def checkWinner(self):
        if (self.board[0] == "X" and self.board[1] == "X" and self.board[2] == "X") or \
        (self.board[3] == "X" and self.board[4] == "X" and self.board[5] == "X") or \
        (self.board[6] == "X" and self.board[7] == "X" and self.board[8] == "X") or \
        (self.board[0] == "X" and self.board[3] == "X" and self.board[6] == "X") or \
        (self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X") or \
        (self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X") or \
        (self.board[0] == "X" and self.board[4] == "X" and self.board[8] == "X") or \
        (self.board[2] == "X" and self.board[4] == "X" and self.board[6] == "X"):
            print (self.player1 + " WINS!")
            return True  
        
        if (self.board[0] == "O" and self.board[1] == "O" and self.board[2] == "O") or \
        (self.board[3] == "O" and self.board[4] == "O" and self.board[5] == "O") or \
        (self.board[6] == "O" and self.board[7] == "O" and self.board[8] == "O") or \
        (self.board[0] == "O" and self.board[3] == "O" and self.board[6] == "O") or \
        (self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O") or \
        (self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O") or \
        (self.board[0] == "O" and self.board[4] == "O" and self.board[8] == "O") or \
        (self.board[2] == "O" and self.board[4] == "O" and self.board[6] == "O"):
            print (self.player2 + " WINS!!!")
            return True    
        
    def PlayGame(self):
        while self.play_ == True:
            if self.IsBoardComplete():
                self.play_ = False
                break
                
            while True:
                try:
                    xTurn = int(input("Enter location for X : "))
                except:
                    print("Invalid input! Enter value from 1 to 9!")
                    continue
                else:
                    if xTurn not in range(1,10):
                        print("Invalid input! Enter value from 1 to 9!")
                        continue
                    elif self.board[xTurn - 1] == "X" or self.board[xTurn - 1] == "O":
                        print ("cell is not empty!")
                        continue
                    else:
                        self.GetTurn("X",xTurn)
                        os.system("cls")
                        self.Header()
                        self.PrintBoard()
                        break
          
            if self.checkWinner() == True:
                self.play_ = False
                break
                
            if self.IsBoardComplete():
                self.play_ = False
                break
            
            while True:
                try:                  
                    oTurn = int(input("Enter location for O : "))
                except:
                    print("Invalid input! Enter value from 1 to 9!")
                    continue
                else:
                    if oTurn not in range(1,10):
                        print("Invalid input! Enter value from 1 to 9!")
                        continue
                    elif self.board[oTurn - 1] == "X" or self.board[oTurn - 1] == "O":
                        print ("cell is not empty!")
                        continue
                    else:
                        self.GetTurn("O",oTurn)
                        os.system("cls")
                        self.Header()
                        self.PrintBoard()
                        break      
                        
            if self.checkWinner() == True:
                self.play_ = False
                break
            
            if self.IsBoardComplete():
                self.play_ = False
                break

        print ("GAME OVER!")
        self.PlayAgain()
        
    def PlayAgain(self):
        playAgain = str(input("\n---------------------------------\n[y] - play again\n"))
        if playAgain.upper() == "Y":
            self.play_ = True
            self.ResetBoard()
            os.system("cls")
            TicTacPy()
        else:
            input("press enter to quit . . .")

                     
main = TicTacPy()
