blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:
    def __init__(self, color, board, position):
        self._color = color
        self._position = position
        self.__board = board
        self.positionX = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.positionY = [1, 2, 3, 4, 5, 6, 7, 8]

    def chess_board(self):
        cross_product = []
        for X in self.positionX:
            for Y in self.positionY:
                cross_product.append((X, Y))
        return cross_product

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value in self.chess_board():
            self._position = value

    def check_move(self, dest):
        return dest not in self.__board.pos_lst in self.chess_board()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__

    def get_icon(self):
        if self.color == "White":
            return whiteIcons[self.get_name()]
        elif self.color == "Black":
            return blackIcons[self.get_name()]


class Knight(Piece):
    def __init__(self, color, board1, position):
        super().__init__(color, board1, position)

    def moves_for_knight(self):
        possible_moves = []
        pst = self.position
        lst = (
            (chr(ord(pst[0] - 1)), pst[1] + 2), (chr(ord(pst[0] + 1)), pst[1] + 2), (chr(ord(pst[0] - 1)), pst[1] - 2),
            (chr(ord(pst[0] + 1)), pst[1] - 2), (chr(ord(pst[0] + 2)), pst[1] + 1), (chr(ord(pst[0] + 2)), pst[1] - 1),
            (chr(ord(pst[0] - 2)), pst[1] + 1), (chr(ord(pst[0] - 2)), pst[1] - 1)
        )
        for tpl in lst:
            if tpl in self.chess_board():
                possible_moves.append(tpl)
        return possible_moves

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_knight()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__


class Rook(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def moves_for_rook(self):
        possible_moves = []
        x = self.positionX
        x.remove(self.position[0])
        y = self.positionY
        y.remove(self.position[1])
        for char in x:
            possible_moves.append((char, self.position[1]))
        for num in y:
            possible_moves.append((self.position[0], num))
        return possible_moves

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_rook()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__


class Bishop(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def moves_for_bishop(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        for num in range(0, 7):
            x = chr(ord(x)+1)
            y = y+1
            if (x, y) in self.chess_board():
                possible_moves.append((x, y))
        x = self.position[0]
        y = self.position[1]
        for num in range(0, 7):
            x = chr(ord(x)-1)
            y = y+1
            if (x, y) in self.chess_board():
                possible_moves.append((x, y))
        x = self.position[0]
        y = self.position[1]
        for num in range(0, 7):
            x = chr(ord(x)-1)
            y = y-1
            if (x, y) in self.chess_board():
                possible_moves.append((x, y))
        x = self.position[0]
        y = self.position[1]
        for num in range(0, 7):
            x = chr(ord(x)+1)
            y = y-1
            if (x, y) in self.chess_board():
                possible_moves.append((x, y))
        return possible_moves

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_bishop

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__


class Queen(Bishop, Rook):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def moves_for_queen(self):
        return self.moves_for_bishop() + self.moves_for_rook()

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_queen()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__


class King(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def moves_for_king(self):
        possible_moves = []
        pst = self.position
        lst = (
               (pst[0], pst[1] + 1), ((chr(ord(pst[0]) - 1)), pst[1] + 1), ((chr(ord(pst[0]) + 1)), pst[1] + 1),
               ((chr(ord(pst[0]) - 1)), pst[1]), ((chr(ord(pst[0]) + 1)), pst[1]), (pst[0], pst[1] - 1),
               ((chr(ord(pst[0]) - 1)), pst[1] - 1), ((chr(ord(pst[0]) + 1)), pst[1] - 1)
        )

        for tpl in lst:
            if tpl in self.chess_board():
                possible_moves.append(tpl)
        return possible_moves

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_king()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__


class Pawn(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def moves_for_pawn(self):
        possible_moves = []
        pst = self.position
        lst = (
            (pst[0], pst[1] + 1), (pst[0], pst[1] + 2),
        )
        for tpl in lst:
            if tpl in self.chess_board():
                possible_moves.append(tpl)
        return possible_moves

    def kill_for_pawn(self):
        possible_kills = []
        pst = self.position
        lst = (
            ((chr(ord(pst[0]) - 1)), pst[1] + 1),
            ((chr(ord(pst[0]) + 1)), pst[1] + 1)
        )
        for tpl in lst:
            if tpl in self.chess_board():
                possible_kills.append(tpl)
        return possible_kills

    def check_move(self, dest):
        return dest not in self.__board.pos_lst and dest in self.moves_for_pawn()

    def move(self, dest):
        if self.check_move(dest):
            self.position(dest)
            return True
        elif dest in self.kill_for_pawn():
            if self.color == "White" and dest in self.__board.pos_blk_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_blk_lst.remove(self.position)
            elif self.color == "Black" and dest in self.__board.pos_wht_lst:
                self.__board.lst.remove(self.__board.get_piece(dest))
                self.__board.pos_lst.remove(self.position)
                self.__board.pos_wht_lst.remove(self.position)
            return True
        else:
            return False

    def get_name(self):
        return self.__class__.__name__
