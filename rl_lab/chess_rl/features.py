import numpy as np

import chess


PIECE_TO_PLANE = {
    chess.Piece(chess.PAWN, chess.WHITE): 0,
    chess.Piece(chess.KNIGHT, chess.WHITE): 1,
    chess.Piece(chess.BISHOP, chess.WHITE): 2,
    chess.Piece(chess.ROOK, chess.WHITE): 3,
    chess.Piece(chess.QUEEN, chess.WHITE): 4,
    chess.Piece(chess.KING, chess.WHITE): 5,
    chess.Piece(chess.PAWN, chess.BLACK): 6,
    chess.Piece(chess.KNIGHT, chess.BLACK): 7,
    chess.Piece(chess.BISHOP, chess.BLACK): 8,
    chess.Piece(chess.ROOK, chess.BLACK): 9,
    chess.Piece(chess.QUEEN, chess.BLACK): 10,
    chess.Piece(chess.KING, chess.BLACK): 11,
}

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0,
}


def board_to_tensor(board: chess.Board) -> np.ndarray:
    tensor = np.zeros((12, 8, 8), dtype=np.float32)
    for square, piece in board.piece_map().items():
        plane = PIECE_TO_PLANE[piece]
        row = 7 - chess.square_rank(square)
        col = chess.square_file(square)
        tensor[plane, row, col] = 1.0
    return tensor


def material_score(board: chess.Board) -> int:
    score = 0
    for piece in board.piece_map().values():
        value = PIECE_VALUES[piece.piece_type]
        score += value if piece.color == chess.WHITE else -value
    return score


def material_label(board: chess.Board) -> str:
    score = material_score(board)
    if score == 0:
        return "material equal"
    leader = "white" if score > 0 else "black"
    return f"{leader} ahead by {abs(score)}"
