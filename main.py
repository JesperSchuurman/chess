class Piece:
    NONE = 0
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

    WHITE = 0
    BLACK = 8

    WhitePawn = PAWN | WHITE  # 1
    WhiteKnight = KNIGHT | WHITE  # 2
    WhiteBishop = BISHOP | WHITE  # 3
    WhiteRook = ROOK | WHITE  # 4
    WhiteQueen = QUEEN | WHITE  # 5
    WhiteKing = KING | WHITE  # 6

    BlackPawn = PAWN | BLACK  # 9
    BlackKnight = KNIGHT | BLACK  # 10
    BlackBishop = BISHOP | BLACK  # 11
    BlackRook = ROOK | BLACK  # 12
    BlackQueen = QUEEN | BLACK  # 13
    BlackKing = KING | BLACK  # 14

    MaxPieceIndex = BlackKing

    PieceIndices = [WhitePawn, WhiteKnight, WhiteBishop, WhiteRook, WhiteQueen, WhiteKing,
                    BlackPawn, BlackKnight, BlackBishop, BlackRook, BlackQueen]

    
