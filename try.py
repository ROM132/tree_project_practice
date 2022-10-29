import random


class Tic_tac_toe:
    choice = {
        1: [1, "#", False],
        2: [2, "#", False],
        3: [3, "#", False],
        4: [4, "#", False],
        5: [5, "#", False],
        6: [6, "#", False],
        7: [7, "#", False],
        8: [8, "#", False],
        9: [9, "#", False],
    }

    def __init__(self, random_choice=None, number=0):
        self.x = "X"
        self.o = "O"

        self.random_choice = random_choice
        self.number = number

    def start_game(self):
        t.winner()

        qus = input("Enter a number between 1-9: ")
        if qus.isdigit():
            qus = int(qus)
        val = self.choice.get(qus)
        if val is None:
            print(f"Invalid input!")
            t.start_game()
        else:
            if qus == self.choice[qus][0]:
                if qus == self.choice[qus][0]:
                    t.checker(self.choice[qus][2])
                    if self.number % 2 == 0:
                        self.choice[qus][1] = self.x
                        self.choice[qus][2] = True
                        self.number += 1
                        t.computer_choice()
                    else:
                        t.print_tic_tac_Toe_board()

                else:
                    print("Error Out of range!")
                    t.start_game()

    def checker(self, i):
        if i is True:
            print("You can't put this in here!")
            t.start_game()

        else:
            pass

    def print_tic_tac_Toe_board(self):
        print(f"{self.choice[1][1]} {self.choice[2][1]} {self.choice[3][1]}\n"
              f"{self.choice[4][1]} {self.choice[5][1]} {self.choice[6][1]}\n"
              f"{self.choice[7][1]} {self.choice[8][1]} {self.choice[9][1]}")
        t.start_game()

    def winner(self):
        if self.choice[1][1] == self.x and self.choice[2][1] == self.x and self.choice[3][1] == self.x or self.choice[4][1] == self.x and self.choice[5][1] == self.x and self.choice[6][1] == self.x or self.choice[7][1] == self.x and self.choice[8][1] == self.x and self.choice[9][1] == self.x or self.choice[1][1] == self.x and self.choice[4][1] == self.x and self.choice[7][1] == self.x or self.choice[2][1] == self.x and self.choice[5][1] == self.x and self.choice[8][1] == self.x or self.choice[3][1] == self.x and self.choice[6][1] == self.x and self.choice[9][1] == self.x or self.choice[1][1] == self.x and self.choice[5][1] == self.x and self.choice[9][1] == self.x or self.choice[3][1] == self.x and self.choice[5][1] == self.x and self.choice[7][1] == self.x:
            print("X Won the game!")
            exit()
        elif self.choice[1][1] == self.o and self.choice[2][1] == self.o and self.choice[3][1] == self.o or self.choice[4][1] == self.o and self.choice[5][1] == self.o and self.choice[6][1] == self.o or self.choice[7][1] == self.o and self.choice[8][1] == self.o and self.choice[9][1] == self.o or self.choice[1][1] == self.o and self.choice[4][1] == self.o and self.choice[7][1] == self.o or self.choice[2][1] == self.o and self.choice[5][1] == self.o and self.choice[8][1] == self.o or self.choice[3][1] == self.o and self.choice[6][1] == self.o and self.choice[9][1] == self.o or self.choice[1][1] == self.o and self.choice[5][1] == self.o and self.choice[9][1] == self.o or self.choice[3][1] == self.o and self.choice[5][1] == self.o and self.choice[7][1] == self.o:
            print("O Won the game!")
            exit()
        elif self.number == 9:
            print("Its a draw!")
            exit()
        else:
            pass

    def computer_choice(self):
        num = random.randint(1, 9)
        if self.number % 2 == 1:
            if self.choice[num][2] is False:
                self.choice[num][1] = self.o
                self.number += 1
                self.choice[num][2] = True
                t.print_tic_tac_Toe_board()
            else:
                t.computer_choice()
        else:
            pass


t = Tic_tac_toe()
t.start_game()
