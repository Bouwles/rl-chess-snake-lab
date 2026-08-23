import chess


PIECE_FAMILIES = {
    chess.PAWN: "pawn",
    chess.KNIGHT: "knight",
    chess.BISHOP: "bishop",
    chess.ROOK: "rook",
    chess.QUEEN: "queen",
    chess.KING: "king",
}


def piece_family(piece: chess.Piece) -> str:
    return PIECE_FAMILIES[piece.piece_type]
