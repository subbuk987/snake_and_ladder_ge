import random

position = 0  # Position of Single Player
total_rolls = 0


def snake_and_ladder():
    global position
    global total_rolls
    while position != 100:
        outcome = random.randint(1, 6)
        total_rolls += 1
        option = random.randint(1, 3)  # 1 - NoPlay, 2 - Ladder, 3 - Snake
        if option == 2:
            position += outcome
            if position > 100:
                position -= outcome

        elif option == 3:
            position -= outcome
            if position < 0:
                position = 0

        print(f"The position after {total_rolls} rolls is: {position}")

    print(f"The total rolls to win: {total_rolls}")


if __name__ == "__main__":
    snake_and_ladder()
