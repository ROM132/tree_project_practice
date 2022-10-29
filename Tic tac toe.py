import random
import time


class Tic_tac_toe:

    def __init__(self, random_choice=None, number=0):
        self.x = "X"
        self.o = "O"

        self.random_choice = random_choice

        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None
        self.six = None
        self.seven = None
        self.eight = None
        self.nine = None
        self.number = number

    def start_game(self):
        t.win_checker1()
        t.computer_choice()

        qus = input("Enter a number between 1-9: ")
        if qus == "1":
            t.checker(self.one)
            if self.number % 2 == 0:
                self.one = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "2":
            t.checker(self.two)
            if self.number % 2 == 0:
                self.two = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "3":
            t.checker(self.three)
            if self.number % 2 == 0:
                self.three = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "4":
            t.checker(self.four)
            if self.number % 2 == 0:
                self.four = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "5":
            t.checker(self.five)
            if self.number % 2 == 0:
                self.five = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "6":
            t.checker(self.six)
            if self.number % 2 == 0:
                self.six = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "7":
            t.checker(self.seven)
            if self.number % 2 == 0:
                self.seven = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        elif qus == "8":
            t.checker(self.eight)
            if self.number % 2 == 0:
                self.eight = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()
        elif qus == "9":
            t.checker(self.nine)
            if self.number % 2 == 0:
                self.nine = self.x
                t.print_tic_tac_Toe_board()
            else:
                t.print_tic_tac_Toe_board()

        else:
            print("Error Out of range!")
            t.start_game()

    def checker(self, i):
        if i is not None:
            print("You can't put this in here!")
            t.start_game()

        else:
            pass

    def computer_choice(self):
        print("\n\n")
        if self.number == 1 or self.number == 3 or self.number == 5 or self.number == 7:
            self.random_choice = [self.one, self.two, self.three, self.four, self.five, self.six,
                                  self.seven, self.eight, self.nine]
            self.random_choice = random.choice(self.random_choice)
            if self.random_choice is None:
                if self.random_choice == self.two:
                    self.two = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.five:
                    self.five = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.one:
                    self.one = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.four:
                    self.four = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.three:
                    self.three = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.nine:
                    self.nine = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.eight:
                    self.eight = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.six:
                    self.six = self.o
                    t.print_tic_tac_Toe_board()
                elif self.random_choice == self.seven:
                    self.seven = self.o
                    t.print_tic_tac_Toe_board()
                else:
                    print("We have a problem!!==========================")
            else:
                t.computer_choice()
        else:
            pass

    def win_checker1(self):
        if self.one == self.x and self.two == self.x and self.three == self.x:
            print("X Won the game")
            exit()
        elif self.four == self.x and self.five == self.x and self.six == self.x:
            print("X Won the game")
            exit()
        elif self.seven == self.x and self.eight == self.x and self.nine == self.x:
            print("X Won the game")
            exit()
        elif self.one == self.x and self.four == self.x and self.seven == self.x:
            print("X Won the game")
            exit()
        elif self.two == self.x and self.five == self.x and self.eight == self.x:
            print("X Won the game")
            exit()
        elif self.three == self.x and self.six == self.x and self.nine == self.x:
            print("X Won the game")
            exit()
        elif self.one == self.x and self.five == self.x and self.nine == self.x:
            print("X Won the game")
            exit()
        elif self.three == self.x and self.five == self.x and self.seven == self.x:
            print("X Won the game")
            exit()

        elif self.one == self.o and self.two == self.o and self.three == self.o:
            print("O Won the game")
            exit()
        elif self.four == self.o and self.five == self.o and self.six == self.o:
            print("O Won the game")
            exit()
        elif self.seven == self.o and self.eight == self.o and self.nine == self.o:
            print("O Won the game")
            exit()
        elif self.one == self.o and self.four == self.o and self.seven == self.o:
            print("O Won the game")
            exit()
        elif self.two == self.o and self.five == self.o and self.eight == self.o:
            print("O Won the game")
            exit()
        elif self.three == self.o and self.six == self.o and self.nine == self.o:
            print("O Won the game")
            exit()
        elif self.one == self.o and self.five == self.o and self.nine == self.o:
            print("O Won the game")
            exit()
        elif self.three == self.o and self.five == self.o and self.seven == self.o:
            print("O Won the game")
            exit()
        else:
            pass

    def print_tic_tac_Toe_board(self):
        self.number += 1
        print(f"{self.one} {self.two} {self.three}\n"
              f"{self.four} {self.five} {self.six}\n"
              f"{self.seven} {self.eight} {self.nine}")

        t.start_game()


t = Tic_tac_toe()
t.start_game()
