from player import Player
import random


class Game:

    # constructor, self is implicit
    def __init__(self, board_size):
        # put board_size here until can figure out how to do class level vars
        self.board_size = board_size
        self.board = ['-'] * self.board_size  # initialize length of list?
        self.clear_board()
        self.taken = 0
        self.player_x = Player(0, 0, 0, 'X', 0)
        self.player_o = Player(0, 0, 0, 'O', 0)
        self.turn = int(0)

    def clear_board(self):
        self.board.clear()
        self.board = ['-'] * self.board_size
        self.taken = 0

    @staticmethod
    def print_board_help():
        print("Board Layout\n")
        print(" 1 | 2 | 3 \n----------- \n 4 | 5 | 6 \n----------- \n 7 | 8 | 9 \n")
        print("***********\n")

    def print_board(self):
        print("\n", self.board[0], '|', self.board[1], '|', self.board[2], "\n",
              self.board[3], '|', self.board[4], '|', self.board[5], "\n",
              self.board[6], '|', self.board[7], '|', self.board[8], "\n")

    def check_if_win(self, p):
        i = 0
        # really wanna find a better algorithm here
        # check row
        while i <= 7:
            if (self.board[i] == p.piece) & (self.board[i+1] == p.piece) & (self.board[i+2] == p.piece):
                self.result_win(p)
                return 1
            i += 3
        # check column
        i = 0
        while i <= 2:
            if (self.board[i] == p.piece) & (self.board[i + 3] == p.piece) & (self.board[i + 6] == p.piece):
                self.result_win(p)
                return 1
            i += 1
        # check diagonal
        if (self.board[0] == p.piece) & (self.board[4] == p.piece) & (self.board[8] == p.piece):
            self.result_win(p)
            return 1
        if (self.board[2] == p.piece) & (self.board[4] == p.piece) & (self.board[6] == p.piece):
            self.result_win(p)
            return 1
        # check stalemate
        if self.taken == self.board_size:
            self.result_stalemate()
            return 1

    def first_pick(self):
        self.turn = random.randint(0, 1)

    def get_choice(self):
        choice = 0
        while choice == 0:
            choice = int(input("Enter spot to place your piece: \n"))
            if (choice < 1) | (choice > self.board_size):
                print("INVALID SPOT: Try again, enter 1-9\n")
                choice = 0
            elif self.board[choice - 1] != '-':
                print("SPOT ALREADY TAKEN: Try again")
                choice = 0
        return choice

    def place_choice(self, p, choice):
        self.board[choice - 1] = p.piece
        self.taken += 1

    def print_score(self):
        print("X Wins: ", self.player_x.wins,
              "Losses: ", self.player_x.losses,
              "Ties: ", self.player_x.ties)
        print("O Wins: ", self.player_o.wins,
              "Losses: ", self.player_o.losses,
              "Ties: ", self.player_o.ties)

    def result_stalemate(self):
        print("STALEMATE!\n")
        self.player_o.ties += 1
        self.player_x.ties += 1

    def result_win(self, p):
        print(p.piece, "'s Win!\n")
        p.wins += 1
        if p.piece == 'X':
            self.player_o.losses += 1
        else:
            self.player_x.losses += 1
