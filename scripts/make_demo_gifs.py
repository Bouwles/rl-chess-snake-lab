from pathlib import Path

import chess
from PIL import Image, ImageDraw, ImageFont

from rl_lab.chess_rl.demo import run_chess_demo
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
        img = Image.new("RGB", (480, 540), "#f7f9fc")
        draw = ImageDraw.Draw(img)
        draw.text((28, 18), "Snake DQN Environment Demo", fill="#17202a", font=font(24))
        draw.text((28, 50), f"Score: {env.score}", fill="#4d5b6c", font=font(18))

        cell = 42
        ox, oy = 28, 90
        draw.rounded_rectangle((ox - 8, oy - 8, ox + 10 * cell + 8, oy + 10 * cell + 8), radius=12, fill="#ffffff", outline="#d4dce8")

        for y in range(env.size):
            for x in range(env.size):
                x0 = ox + x * cell
                y0 = oy + y * cell
                draw.rectangle((x0, y0, x0 + cell - 3, y0 + cell - 3), fill="#edf2f7")

        for index, (x, y) in enumerate(env.snake):
            color = "#1f6feb" if index == 0 else "#63a4ff"
            draw.rounded_rectangle((ox + x * cell, oy + y * cell, ox + x * cell + cell - 3, oy + y * cell + cell - 3), radius=8, fill=color)

        fx, fy = env.food
        draw.ellipse((ox + fx * cell + 8, oy + fy * cell + 8, ox + fx * cell + cell - 11, oy + fy * cell + cell - 11), fill="#e63946")

        frames.append(img)
        _, _, done, _ = env.step([1, 1, 2, 1, 0, 1][step % 6])
        if done:
            env.reset()

    frames[0].save(MEDIA_DIR / "snake_demo.gif", save_all=True, append_images=frames[1:], duration=140, loop=0)


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
            x = ox + file * square + 16
            y = oy + rank * square + 13
            draw.text((x, y), piece.symbol(), fill="#17202a", font=font(28))

        frames.append(img)
        if index < len(moves):
            board.push(chess.Move.from_uci(moves[index]))

    frames[0].save(MEDIA_DIR / "chess_demo.gif", save_all=True, append_images=frames[1:], duration=700, loop=0)


if __name__ == "__main__":
    make_snake_demo()
    make_chess_demo()
    print("Created demo GIFs in docs/media")
