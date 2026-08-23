from pathlib import Path

import chess
from PIL import Image, ImageDraw, ImageFont

from rl_lab.chess_rl.demo import run_chess_demo
from rl_lab.chess_rl.rendering import piece_family
from rl_lab.snake.env import SnakeEnv


MEDIA_DIR = Path("docs/media")
MEDIA_DIR.mkdir(parents=True, exist_ok=True)


def font(size: int):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


def make_snake_demo() -> None:
    env = SnakeEnv(size=10, seed=4)
    frames = []
    env.reset()

    for step in range(36):
        img = Image.new("RGB", (480, 540), "#eef4f8")
        draw = ImageDraw.Draw(img)
        draw.text((28, 18), "Snake DQN Environment Demo", fill="#17202a", font=font(24))
        draw.text((28, 50), f"Score: {env.score}", fill="#4d5b6c", font=font(18))

        cell = 42
        ox, oy = 28, 90
        draw.rounded_rectangle((ox - 10, oy - 10, ox + 10 * cell + 10, oy + 10 * cell + 10), radius=18, fill="#19324a", outline="#102235")

        for y in range(env.size):
            for x in range(env.size):
                x0 = ox + x * cell
                y0 = oy + y * cell
                color = "#d7f0dc" if (x + y) % 2 == 0 else "#c6e6cd"
                draw.rounded_rectangle((x0, y0, x0 + cell - 4, y0 + cell - 4), radius=5, fill=color)

        for index, (x, y) in enumerate(env.snake):
            x0 = ox + x * cell
            y0 = oy + y * cell
            color = "#12664f" if index == 0 else "#22a06b"
            draw.rounded_rectangle((x0 + 3, y0 + 3, x0 + cell - 7, y0 + cell - 7), radius=13, fill=color)
            if index == 0:
                draw.ellipse((x0 + 11, y0 + 12, x0 + 17, y0 + 18), fill="white")
                draw.ellipse((x0 + 25, y0 + 12, x0 + 31, y0 + 18), fill="white")
                draw.ellipse((x0 + 13, y0 + 14, x0 + 16, y0 + 17), fill="#111827")
                draw.ellipse((x0 + 27, y0 + 14, x0 + 30, y0 + 17), fill="#111827")

        fx, fy = env.food
        apple_x = ox + fx * cell
        apple_y = oy + fy * cell
        draw.ellipse((apple_x + 8, apple_y + 10, apple_x + cell - 11, apple_y + cell - 8), fill="#d62828")
        draw.rectangle((apple_x + 20, apple_y + 7, apple_x + 24, apple_y + 15), fill="#6b3f1d")
        draw.ellipse((apple_x + 24, apple_y + 6, apple_x + 33, apple_y + 14), fill="#2f9e44")

        frames.append(img)
        _, _, done, _ = env.step([1, 1, 2, 1, 0, 1][step % 6])
        if done:
            env.reset()

    frames[0].save(MEDIA_DIR / "snake_demo.gif", save_all=True, append_images=frames[1:], duration=140, loop=0)


def draw_chess_piece(draw: ImageDraw.ImageDraw, piece: chess.Piece, x: int, y: int, square: int) -> None:
    family = piece_family(piece)
    fill = "#f8fafc" if piece.color == chess.WHITE else "#111827"
    outline = "#111827" if piece.color == chess.WHITE else "#f8fafc"
    cx = x + square // 2
    base_y = y + square - 11

    draw.ellipse((cx - 13, y + 11, cx + 13, y + 37), fill=fill, outline=outline, width=2)
    draw.rounded_rectangle((cx - 18, y + 32, cx + 18, base_y - 7), radius=6, fill=fill, outline=outline, width=2)
    draw.rectangle((cx - 24, base_y - 7, cx + 24, base_y), fill=fill, outline=outline, width=2)

    if family == "king":
        draw.line((cx, y + 5, cx, y + 22), fill=outline, width=3)
        draw.line((cx - 7, y + 12, cx + 7, y + 12), fill=outline, width=3)
    elif family == "queen":
        for offset in (-13, 0, 13):
            draw.ellipse((cx + offset - 4, y + 4, cx + offset + 4, y + 12), fill=outline)
    elif family == "rook":
        for offset in (-14, 0, 14):
            draw.rectangle((cx + offset - 5, y + 7, cx + offset + 5, y + 18), fill=outline)
    elif family == "bishop":
        draw.line((cx - 8, y + 15, cx + 8, y + 28), fill=outline, width=3)
    elif family == "knight":
        draw.polygon(
            [(cx - 13, y + 18), (cx + 10, y + 8), (cx + 17, y + 30), (cx - 5, y + 34)],
            fill=fill,
            outline=outline,
        )
        draw.ellipse((cx + 5, y + 19, cx + 9, y + 23), fill=outline)
    elif family == "pawn":
        draw.ellipse((cx - 9, y + 16, cx + 9, y + 34), fill=fill, outline=outline, width=2)


def make_chess_demo() -> None:
    board = chess.Board()
    frames = []
    moves = run_chess_demo(plies=12)
    square = 54
    ox, oy = 24, 74

    for index, move_uci in enumerate(["start", *moves]):
        img = Image.new("RGB", (500, 560), "#f7f9fc")
        draw = ImageDraw.Draw(img)
        draw.text((24, 18), "Chess Self-Play Demo", fill="#17202a", font=font(24))
        draw.text((24, 48), f"Move: {move_uci}", fill="#4d5b6c", font=font(18))

        for rank in range(8):
            for file in range(8):
                color = "#f0d9b5" if (rank + file) % 2 == 0 else "#b58863"
                x0 = ox + file * square
                y0 = oy + rank * square
                draw.rectangle((x0, y0, x0 + square, y0 + square), fill=color)

        for sq, piece in board.piece_map().items():
            file = chess.square_file(sq)
            rank = 7 - chess.square_rank(sq)
            draw_chess_piece(draw, piece, ox + file * square, oy + rank * square, square)

        frames.append(img)
        if index < len(moves):
            board.push(chess.Move.from_uci(moves[index]))

    frames[0].save(MEDIA_DIR / "chess_demo.gif", save_all=True, append_images=frames[1:], duration=700, loop=0)


if __name__ == "__main__":
    make_snake_demo()
    make_chess_demo()
    print("Created demo GIFs in docs/media")
