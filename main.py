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
        self.white_pieces.board |= self.white_pawn.get_bitboard()
        self.white_pieces.board |= self.white_knight.get_bitboard()
        self.white_pieces.board |= self.white_bishop.get_bitboard()
        self.white_pieces.board |= self.white_rook.get_bitboard()
        self.white_pieces.board |= self.white_queen.get_bitboard()
        self.white_pieces.board |= self.white_king.get_bitboard()

        self.black_pieces.board |= self.black_pawn.get_bitboard()
        self.black_pieces.board |= self.black_knight.get_bitboard()
        self.black_pieces.board |= self.black_bishop.get_bitboard()
        self.black_pieces.board |= self.black_rook.get_bitboard()
        self.black_pieces.board |= self.black_queen.get_bitboard()
        self.black_pieces.board |= self.black_king.get_bitboard()

        self.all_pieces.board |= self.white_pieces.get_bitboard()
        self.all_pieces.board |= self.black_pieces.get_bitboard()

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
        self.is_white_turn = True

    def print_state(self):
        self.board.print_board()

    def standard_setup(self):
        self.board.setup_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")

    def custom_setup(self, fen):
        self.board.setup_board(fen)

    def make_move(self, start_square, move):
        algebraic_move = convert_algebraic_to_int(move)

        start_square = int(start_square)

        if algebraic_move[0] == "P":
            moves = self.generate_pawn_moves(start_square)
        elif algebraic_move[0] == "N":
            moves = self.generate_knight_moves(start_square)
        elif algebraic_move[0] == "B":
            moves = self.generate_bishop_moves(start_square)
        elif algebraic_move[0] == "R":
            moves = self.generate_rook_moves(start_square)
        elif algebraic_move[0] == "Q":
            moves = self.generate_queen_moves(start_square)
        else:
            moves = self.generate_king_moves(start_square)

        if algebraic_move[1] in moves:
            if algebraic_move[0] == "P":
                self.board.white_pawn.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_pawn.set_square(algebraic_move[1])
                self.board.white_pawn.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_pawn.clear_square(start_square)
            elif algebraic_move[0] == "N":
                self.board.white_knight.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_knight.set_square(algebraic_move[1])
                self.board.white_knight.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_knight.clear_square(start_square)
            elif algebraic_move[0] == "B":
                self.board.white_bishop.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_bishop.set_square(algebraic_move[1])
                self.board.white_bishop.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_bishop.clear_square(start_square)
            elif algebraic_move[0] == "R":
                self.board.white_rook.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_rook.set_square(algebraic_move[1])
                self.board.white_rook.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_rook.clear_square(start_square)
            elif algebraic_move[0] == "Q":
                self.board.white_queen.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_queen.set_square(algebraic_move[1])
                self.board.white_queen.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_queen.clear_square(start_square)
            else:
                self.board.white_king.set_square(algebraic_move[1]) if self.is_white_turn \
                    else self.board.black_king.set_square(algebraic_move[1])
                self.board.white_king.clear_square(start_square) if self.is_white_turn \
                    else self.board.black_king.clear_square(start_square)
            if move.__contains__("x"):
                # taking pawns
                if self.board.white_pawn.is_square_set(algebraic_move[1]):
                    self.board.white_pawn.clear_square(algebraic_move[1])
                elif self.board.black_pawn.is_square_set(algebraic_move[1]):
                    self.board.black_pawn.clear_square(algebraic_move[1])
                # taking knights
                elif self.board.white_knight.is_square_set(algebraic_move[1]):
                    self.board.white_knight.clear_square(algebraic_move[1])
                elif self.board.black_knight.is_square_set(algebraic_move[1]):
                    self.board.black_knight.clear_square(algebraic_move[1])
                # taking bishops
                elif self.board.white_bishop.is_square_set(algebraic_move[1]):
                    self.board.white_bishop.clear_square(algebraic_move[1])
                elif self.board.black_bishop.is_square_set(algebraic_move[1]):
                    self.board.black_bishop.clear_square(algebraic_move[1])
                # taking rooks
                elif self.board.white_rook.is_square_set(algebraic_move[1]):
                    self.board.white_rook.clear_square(algebraic_move[1])
                elif self.board.black_rook.is_square_set(algebraic_move[1]):
                    self.board.black_rook.clear_square(algebraic_move[1])
                # taking queens
                elif self.board.white_queen.is_square_set(algebraic_move[1]):
                    self.board.white_queen.clear_square(algebraic_move[1])
                elif self.board.black_queen.is_square_set(algebraic_move[1]):
                    self.board.black_queen.clear_square(algebraic_move[1])

            if self.is_white_turn:
                self.is_white_turn = False
            else:
                self.is_white_turn = True
        else:
            print("This isn't a valid move.")

    def generate_pawn_moves(self, pawn_square):
        self.board.get_all_pieces()
        moves = []

        pawn_bitboard = 1 << pawn_square
        opponent_pieces = self.board.black_pieces.get_bitboard() if self.is_white_turn \
            else self.board.white_pieces.get_bitboard()
        all_pieces = self.board.all_pieces.get_bitboard()

        direction = 1 if self.is_white_turn else -1
        starting_rank = 1 if self.is_white_turn else 6

        # single square moves
        if 0 <= pawn_square + 8 * direction <= 63:
            single_moves = (pawn_bitboard << abs(8 * direction)) & ~all_pieces
            if single_moves:
                moves.append(pawn_square + (8 * direction))

        # double square moves
        if pawn_square // 8 == starting_rank:
            double_moves = (pawn_bitboard << abs(16 * direction)) & ~all_pieces
            if double_moves:
                moves.append(pawn_square + (16 * direction))

        # capturing moves
        right_capture_square = pawn_square + (9 * direction)
        left_capture_square = pawn_square + (7 * direction)

        if right_capture_square % 8 != 0:
            if opponent_pieces & (1 << right_capture_square):
                moves.append(right_capture_square)

        if left_capture_square % 8 != 7:
            if opponent_pieces & (1 << left_capture_square):
                moves.append(left_capture_square)

        return moves

    def generate_knight_moves(self, knight_square):
        self.board.get_all_pieces()
        moves = []

        knight_bitboard = 1 << knight_square
        own_pieces = self.board.white_pieces.get_bitboard() if self.is_white_turn \
            else self.board.black_pieces.get_bitboard()

        shift_possibilities = [6, 10, 15, 17]
        file = (knight_square % 8) + 1

        for shift in shift_possibilities:
            # forward knight moves
            forward_destination = knight_square + shift
            if (file <= 2 and shift == 6) or (file == 1 and shift == 15) or (file >= 7 and shift == 10) or \
                    (file == 8 and shift == 17):
                continue

            if forward_destination < 64:
                forward_moves = (knight_bitboard << shift) & ~own_pieces
                if forward_moves:
                    moves.append(forward_destination)

        # backward knight moves
        for shift in shift_possibilities:
            backward_destination = knight_square - shift
            if (file <= 2 and shift == 10) or (file == 1 and shift == 17) or (file >= 7 and shift == 6) or \
                    (file == 8 and shift == 15):
                continue

            if backward_destination >= 0:
                backward_moves = (knight_bitboard >> shift) & ~own_pieces
                if backward_moves:
                    moves.append(backward_destination)

        return moves

    def generate_bishop_moves(self, bishop_square):
        self.board.get_all_pieces()
        moves = []

        bishop_bitboard = 1 << bishop_square
        own_pieces = self.board.white_pieces.get_bitboard() if self.is_white_turn \
            else self.board.black_pieces.get_bitboard()
        opponent_pieces = self.board.black_pieces.get_bitboard() if self.is_white_turn \
            else self.board.white_pieces.get_bitboard()

        file = (bishop_square % 8) + 1
        last_file = file

        # left forward
        for i in range(1, 8):
            left_forward = (bishop_bitboard << abs(i * 8 - i)) & ~own_pieces

            destination = bishop_square + (i * 8 - i)
            if (last_file - (destination % 8) + 1) == 1:
                if left_forward and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = (destination % 8) + 1
                    if opponent_pieces & (1 << destination):
                        last_file = file
                        break
                else:
                    break
            else:
                last_file = file
                break
        # right forward
        for i in range(1, 8):
            right_forward = (bishop_bitboard << abs(i * 8 + i)) & ~own_pieces

            destination = bishop_square + (i * 8 + i)
            if ((destination % 8) + 1) - last_file == 1:
                if right_forward and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = (destination % 8) + 1
                    if opponent_pieces & (1 << destination):
                        last_file = file
                        break
                else:
                    break
            else:
                last_file = file
                break
        # left backward
        for i in range(1, 8):
            left_backward = (bishop_bitboard >> (i * 8 + i)) & ~own_pieces

            destination = bishop_square - (i * 8 + i)
            if (last_file - (destination % 8) + 1) == 1:
                if left_backward and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = (destination % 8) + 1
                    if opponent_pieces & (1 << destination):
                        last_file = file
                        break
                else:
                    break
            else:
                last_file = file
                break
        # right backward
        for i in range(1, 8):
            right_backward = (bishop_bitboard >> abs(i * 8 - i)) & ~own_pieces

            destination = bishop_square - (i * 8 - i)
            if ((destination % 8) + 1) - last_file == 1:
                if right_backward and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = (destination % 8) + 1
                    if opponent_pieces & (1 << destination):
                        break
                else:
                    break
            else:
                break
        return moves

    def generate_rook_moves(self, rook_square):
        self.board.get_all_pieces()
        moves = []

        rook_bitboard = 1 << rook_square
        own_pieces = self.board.white_pieces.get_bitboard() if self.is_white_turn \
            else self.board.black_pieces.get_bitboard()
        opponent_pieces = self.board.black_pieces.get_bitboard() if self.is_white_turn \
            else self.board.white_pieces.get_bitboard()

        file = (rook_square % 8) + 1
        last_file = file

        # up
        for i in range(1, 8):
            up_move = (rook_bitboard << i * 8) & ~own_pieces

            destination = (rook_square + (8 * i))
            if up_move and 0 <= destination <= 63:
                moves.append(destination)
                if opponent_pieces & (1 << destination):
                    break
            else:
                break
        # down
        for i in range(1, 8):
            down_move = (rook_bitboard >> i * 8) & ~own_pieces

            destination = (rook_square - (8 * i))
            if down_move and 0 <= destination <= 63:
                moves.append(destination)
                if opponent_pieces & (1 << destination):
                    break
            else:
                break

        # right
        for i in range(1, 8):
            right_move = (rook_bitboard << i) & ~own_pieces

            destination = (rook_square + i)
            next_file = (destination % 8) + 1
            if next_file - last_file == 1:
                if right_move and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = next_file
                    if opponent_pieces & (1 << destination):
                        last_file = file
                        break
                else:
                    break
            else:
                last_file = file
                break

        # left
        for i in range(1, 8):
            left_move = (rook_bitboard >> i) & ~own_pieces

            destination = (rook_square - i)
            next_file = (destination % 8) + 1
            if last_file - next_file == 1:
                if left_move and 0 <= destination <= 63:
                    moves.append(destination)
                    last_file = next_file
                    if opponent_pieces & (1 << destination):
                        break
                else:
                    break
            else:
                break

        return moves

    def generate_queen_moves(self, queen_square):
        moves = []

        moves.extend(self.generate_bishop_moves(queen_square))
        moves.extend(self.generate_rook_moves(queen_square))

        return moves

    def generate_king_moves(self, king_square):
        self.board.get_all_pieces()
        moves = []

        king_bitboard = 1 << king_square
        own_pieces = self.board.white_pieces.get_bitboard() if self.is_white_turn \
            else self.board.black_pieces.get_bitboard()

        shift_possibilities = [1, 7, 8, 9]

        # upper L
        for shift in shift_possibilities:
            king_move = (king_bitboard << abs(-shift)) & ~own_pieces

            if king_move:
                moves.append(king_square + shift)

        # lower L
        for shift in shift_possibilities:
            king_move = (king_bitboard << shift) & ~own_pieces

            if king_move:
                moves.append(king_square - shift)

        return moves


if __name__ == "__main__":
    game = ChessGame()
    game.custom_setup("rnbqkbnr/pppppppp/8/P7/8/P4R2/PPPPPPPP/RNBQKBNR")
    game.print_state()
    count = 0
    while count < 5:
        # game.make_move(input("starting_square:"), input("move:"))
        game.make_move(21, "Rb3")
        game.print_state()
        game.board.black_pawn.print_board()
        count += 1
