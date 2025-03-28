import random

position = 0  # Position of Single Player


def snake_and_ladder():
    global position
    outcome = random.randint(1, 6)
    option = random.randint(1, 3)  # 1 - NoPlay, 2 - Ladder, 3 - Snake
    if option == 2:
        position += outcome
    elif option == 3:
        position -= outcome


if __name__ == "__main__":
    snake_and_ladder()
