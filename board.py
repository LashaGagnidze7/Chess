from pieces import *


class Board:

    def __init__(self):
        self.pw1, self.pw2 = Pawn("White", self, ("A", 2)), Pawn("White", self, ("B", 2))
        self.pw3, self.pw4 = Pawn("White", self, ("C", 2)), Pawn("White", self, ("D", 2))
        self.pw5, self.pw6 = Pawn("White", self, ("E", 2)), Pawn("White", self, ("F", 2))
        self.pw7, self.pw8 = Pawn("White", self, ("G", 2)), Pawn("White", self, ("G", 2))
        self.pb1, self.pb2 = Pawn("Black", self, ("A", 7)), Pawn("Black", self, ("B", 7))
        self.pb3, self.pb4 = Pawn("Black", self, ("C", 7)), Pawn("Black", self, ("D", 7))
        self.pb5, self.pb6 = Pawn("Black", self, ("E", 7)), Pawn("Black", self, ("F", 7))
        self.pb7, self.pb8 = Pawn("Black", self, ("G", 7)), Pawn("Black", self, ("G", 7))
        self.rw1, self.rw2 = Rook("White", self, ("A", 1)), Rook("White", self, ("H", 1))
        self.rb1, self.rb2 = Rook("Black", self, ("A", 8)), Rook("Black", self, ("H", 8))
        self.knw1, self.knw2 = Knight("White", self, ("B", 1)), Knight("White", self, ("G", 1))
        self.knb1, self.knb2 = Knight("Black", self, ("B", 8)), Knight("Black", self, ("G", 8))
        self.bw1, self.bw2 = Bishop("White", self, ("C", 1)), Bishop("White", self, ("F", 1))
        self.bb1, self.bb2 = Bishop("Black", self, ("C", 8)), Bishop("Black", self, ("F", 8))
        self.qw, self.qb = Queen("White", self, ("D", 1)), Queen("Black", self, ("D", 8))
        self.kw, self.kb = King("White", self, ("E", 1)), King("Black", self, ("E", 8))
        self.lst = [self.pw1, self.pw2, self.pw3, self.pw4, self.pw5, self.pw6, self.pw7, self.pw8, self.rw1, self.knw1,
                    self.bw1, self.qw, self.kw, self.bw2, self.knw2, self.rw2, self.pb1, self.pb2, self.pb3, self.pb4,
                    self.pb5, self.pb6, self.pb7, self.pb8, self.rb1, self.knb1, self.bb1, self.qb, self.kb, self.bb2,
                    self.knb2, self.rb2
                    ]

        self.pos_lst = list(map(lambda obj: obj.position, self.lst))
        self.pos_wht_lst = list(map(lambda obj: obj.position, self.lst[:17]))
        self.pos_blk_lst = list(map(lambda obj: obj.position, self.lst[17:]))

        self.row = ["   ", "(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "(7)", "(8)"]
        self.row1 = ["(A)"]
        for piece in self.lst[24:]:
            self.row1.append("[" + str(piece.get_icon()) + "]")
        self.row2 = ["(B)"]
        for figure in self.lst[16:24]:
            self.row2.append("[" + str(figure.get_icon()) + "]")
        self.row3 = ["(C)", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        self.row4 = ["(D)", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        self.row5 = ["(E)", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        self.row6 = ["(F)", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]
        self.row7 = ["(G)"]
        for symbol in self.lst[:8]:
            self.row7.append("[" + str(symbol.get_icon()) + "]")
        self.row8 = ["(H)"]
        for icon in self.lst[8:16]:
            self.row8.append("[" + str(icon.get_icon()) + "]")
        self.rows = [self.row, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7, self.row8]
        self.place_pieces()

    def place_pieces(self):
        return self.rows

    @staticmethod
    def set_piece(position, piece):
        if piece.check_move(position):
            piece.move(position)

    def get_piece(self, position):
        for obj in self.lst:
            if obj.position == position:
                return obj
            else:
                return None

    def make_move(self, start_position, end_position, player):
        if player == "White" and start_position in self.pos_wht_lst:
            self.set_piece(end_position, self.get_piece(start_position))
            self.pos_lst.append(end_position)
            self.pos_wht_lst.append(end_position)
            if self.row1[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row1[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row2[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row2[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row3[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row3[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row4[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row4[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row5[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row5[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row6[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row6[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row7[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row7[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row8[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row8[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
        elif player == "Black" and start_position in self.pos_blk_lst:
            self.set_piece(end_position, self.get_piece(start_position))
            self.pos_lst.append(end_position)
            self.pos_blk_lst.append(end_position)
            if self.row1[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row1[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row2[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row2[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row3[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row3[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row4[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row4[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row5[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row5[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row6[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row6[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row7[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row7[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"
            if self.row8[0] == "(" + str(self.get_piece(end_position).position()[0]) + ")":
                self.row8[self.get_piece(end_position).position()[1]] = "[" + str(
                    self.get_piece(end_position).get_icon()) + "]"

    def display_board(self):
        for index in range(0, 9):
            for paint in self.rows[index]:
                print(paint, end="")
            print("\t")
