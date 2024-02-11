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
        # white pieces
        self.white_pawn = Bitboard()
        self.white_knight = Bitboard()
        self.white_bishop = Bitboard()
        self.white_rook = Bitboard()
        self.white_queen = Bitboard()
        self.white_king = Bitboard()
        self.white_pieces = Bitboard()

        # black pieces
        self.black_pawn = Bitboard()
        self.black_knight = Bitboard()
        self.black_bishop = Bitboard()
        self.black_rook = Bitboard()
        self.black_queen = Bitboard()
        self.black_king = Bitboard()
        self.black_pieces = Bitboard()

        self.all_pieces = Bitboard()

    def setup_board(self, start_position):
        position_by_rank = start_position.split("/")
        count = 56

        for rank in position_by_rank:
            for square in rank:
                if square.isalpha():
                    if square.isupper():
                        if square == "P":
                            self.white_pawn.set_square(count)
                            count += 1
                        elif square == "N":
                            self.white_knight.set_square(count)
                            count += 1
                        elif square == "B":
                            self.white_bishop.set_square(count)
                            count += 1
                        elif square == "R":
                            self.white_rook.set_square(count)
                            count += 1
                        elif square == "Q":
                            self.white_queen.set_square(count)
                            count += 1
                        elif square == "K":
                            self.white_king.set_square(count)
                            count += 1
                    elif square.islower():
                        if square == "p":
                            self.black_pawn.set_square(count)
                            count += 1
                        elif square == "n":
                            self.black_knight.set_square(count)
                            count += 1
                        elif square == "b":
                            self.black_bishop.set_square(count)
                            count += 1
                        elif square == "r":
                            self.black_rook.set_square(count)
                            count += 1
                        elif square == "q":
                            self.black_queen.set_square(count)
                            count += 1
                        elif square == "k":
                            self.black_king.set_square(count)
                            count += 1
                elif square.isdigit():
                    count += int(square)
            count -= 16

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
                found_piece = False
                if self.white_pawn.is_square_set(square):
                    print('P', end=' ')
                    found_piece = True
                elif self.white_knight.is_square_set(square):
                    print('N', end=' ')
                    found_piece = True
                elif self.white_bishop.is_square_set(square):
                    print('B', end=' ')
                    found_piece = True
                elif self.white_rook.is_square_set(square):
                    print('R', end=' ')
                    found_piece = True
                elif self.white_queen.is_square_set(square):
                    print('Q', end=' ')
                    found_piece = True
                elif self.white_king.is_square_set(square):
                    print('K', end=' ')
                    found_piece = True
                elif self.black_pawn.is_square_set(square):
                    print('p', end=' ')
                    found_piece = True
                elif self.black_knight.is_square_set(square):
                    print('n', end=' ')
                    found_piece = True
                elif self.black_bishop.is_square_set(square):
                    print('b', end=' ')
                    found_piece = True
                elif self.black_rook.is_square_set(square):
                    print('r', end=' ')
                    found_piece = True
                elif self.black_queen.is_square_set(square):
                    print('q', end=' ')
                    found_piece = True
                elif self.black_king.is_square_set(square):
                    print('k', end=' ')
                    found_piece = True

                if not found_piece:
                    print('.', end=' ')
            print()

def get_file_as_number(file):
    if file == "a":
        return 0
    elif file == "b":
        return 1
    elif file == "c":
        return 2
    elif file == "d":
        return 3
    elif file == "e":
        return 4
    elif file == "f":
        return 5
    elif file == "g":
        return 6
    elif file == "h":
        return 7

def convert_algebraic_to_int(move):
    destination_square = move[-2:]

    destination_int = get_file_as_number(destination_square[0]) + (int(destination_square[1]) - 1) * 8

    if move[0].islower():
        piece_type = "P"
    else:
        piece_type = move[0]

    return [piece_type, destination_int]

class ChessGame:
    def __init__(self):
        self.board = Chessboard()
        self.is_whites_turn = True

    def print_state(self):
        self.board.print_board()

    def standard_setup(self):
        self.board.setup_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def make_move(self, move):
        algebraic_move = convert_algebraic_to_int(move)

        if self.is_whites_turn:
            if algebraic_move[0] == "P":
                self.board.white_pawn.set_square(algebraic_move[1])


if __name__ == "__main__":
    game = ChessGame()
    game.standard_setup()
    game.print_state()
    game.make_move("e4")
    game.print_state()
