from board import Board
from pieces import *


class Chess:
    def __init__(self):
        self.board = Board()
        self.start = "A1"
        self.end = "H8"
        self.current_player = "White"

    def swap_players(self):
        if self.current_player == "White":
            self.current_player = "Black"
        else:
            self.current_player = "White"

    def is_string_valid_move(self, move_str):
        valid_move = []
        for pos in self.board.pos_lst:
            valid_move.append(pos[0] + str(pos[1]))
        return move_str[0:2] in valid_move and move_str[3:5] in valid_move

    def play(self):
        self.board.display_board()
        try:
            self.start, self.end = input(self.current_player + "\'s turn. Enter a move:").split()
            if self.is_string_valid_move(self.start + " " + self.end):
                self.board.make_move(tuple([self.start[0], int(self.start[1])]), tuple([self.end[0], int(self.end[1])]), self.current_player)
                self.swap_players()
                self.play()
        except:
            print("Invalid input")
        finally:
            self.play()

if __name__ == "__main__":
    game = Chess()
    game.play()