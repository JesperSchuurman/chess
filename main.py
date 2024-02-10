class Bitboard:
    def __init__(self):
        # Initialize an empty bitboard
        self.board = 0

    def set_square(self, square):
        # Set a specific square on the bitboard
        self.board |= 1 << square

    def clear_square(self, square):
        # Clear a specific square on the bitboard
        self.board &= ~(1 << square)

    def is_square_set(self, square):
        # Check if a specific square is set on the bitboard
        return bool(self.board & (1 << square))

    def get_bitboard(self):
        return self.board

    def print_board(self):
        # Print the bitboard in a human-readable format
        for rank in range(7, -1, -1):
            for file in range(8):
                square = rank * 8 + file
                if self.is_square_set(square):
                    print('1', end=' ')
                else:
                    print('0', end=' ')
            print()
class Chessboard:
    def __init__(self):
        #white pieces
        self.white_pawn = Bitboard()
        self.white_knight = Bitboard()
        self.white_bishop = Bitboard()
        self.white_rook = Bitboard()
        self.white_queen = Bitboard()
        self.white_king = Bitboard()
        self.white_pieces = Bitboard()

        #black pieces
        self.black_pawn = Bitboard()
        self.black_knight = Bitboard()
        self.black_bishop = Bitboard()
        self.black_rook = Bitboard()
        self.black_queen = Bitboard()
        self.black_king = Bitboard()
        self.black_pieces = Bitboard()

        self.all_pieces = Bitboard()

    def setup_board(self):
        #set up the white pieces
        self.white_pawn.set_square(2)
        self.white_pawn.set_square(10)
        self.white_pawn.set_square(18)
        self.white_pawn.set_square(26)
        self.white_pawn.set_square(34)
        self.white_pawn.set_square(42)
        self.white_pawn.set_square(50)
        self.white_pawn.set_square(58)

        self.white_knight.set_square(17)
        self.white_knight.set_square(41)

        self.white_bishop.set_square(9)
        self.white_bishop.set_square(49)

        self.white_rook.set_square(1)
        self.white_rook.set_square(57)

        self.white_queen.set_square(25)

        self.white_king.set_square(33)

        #set up the black pieces
        self.black_pawn.set_square(7)
        self.black_pawn.set_square(15)
        self.black_pawn.set_square(23)
        self.black_pawn.set_square(31)
        self.black_pawn.set_square(39)
        self.black_pawn.set_square(47)
        self.black_pawn.set_square(55)
        self.black_pawn.set_square(63)

        self.black_knight.set_square(24)
        self.black_knight.set_square(48)

        self.black_bishop.set_square(16)
        self.black_bishop.set_square(56)

        self.black_rook.set_square(8)
        self.black_rook.set_square(64)

        self.black_queen.set_square(32)

        self.black_king.set_square(40)

    def get_all_pieces(self):
        self.white_pieces |= self.white_pawn.get_bitboard()
        self.white_pieces |= self.white_knight.get_bitboard()
        self.white_pieces |= self.white_bishop.get_bitboard()
        self.white_pieces |= self.white_rook.get_bitboard()
        self.white_pieces |= self.white_queen.get_bitboard()
        self.white_pieces |= self.white_king.get_bitboard()

        self.black_pieces |= self.black_pawn.get_bitboard()
        self.black_pieces |= self.black_knight.get_bitboard()
        self.black_pieces |= self.black_bishop.get_bitboard()
        self.black_pieces |= self.black_rook.get_bitboard()
        self.black_pieces |= self.black_queen.get_bitboard()
        self.black_pieces |= self.black_king.get_bitboard()

        self.all_pieces |= self.white_pieces.get_bitboard()
        self.all_pieces |= self.black_pieces.get_bitboard()

    def print_board(self):
        for rank in range(7, -1, -1):
            for file in range(8):
                square = rank * 8 + file
                if square & self.white_pawn.get_bitboard():
                    print('P', end=' ')
                elif square & self.white_knight.get_bitboard():
                    print('N', end=' ')
                elif square & self.white_bishop.get_bitboard():
                    print('B', end=' ')
                elif square & self.white_rook.get_bitboard():
                    print('R', end=' ')
                elif square & self.white_queen.get_bitboard():
                    print('Q', end=' ')
                elif square & self.white_king.get_bitboard():
                    print('K', end=' ')
                elif square & self.black_pawn.get_bitboard():
                    print('p', end=' ')
                elif square & self.black_knight.get_bitboard():
                    print('n', end=' ')
                elif square & self.black_bishop.get_bitboard():
                    print('b', end=' ')
                elif square & self.black_rook.get_bitboard():
                    print('r', end=' ')
                elif square & self.black_queen.get_bitboard():
                    print('q', end=' ')
                elif square & self.black_king.get_bitboard():
                    print('k', end=' ')
                else:
                    print('.', end=' ')
            print()

class ChessGame:
    def __init__(self):
        self.board = Chessboard()
        self.board.setup_board()

    def print_state(self):
        self.board.get_all_pieces

if __name__ == "__main__":
    board = Chessboard()
    board.setup_board()
    board.print_board()