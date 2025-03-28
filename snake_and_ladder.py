import random

player1_pos = 0  # Position of Player 1
player2_pos = 0  # Position of Player 2
chance = 1
total_rolls = 0


def update(position, option, outcome):
    if option == 2:
        position += outcome
        if position > 100:
            position -= outcome

    elif option == 3:
        position -= outcome
        if position < 0:
            position = 0

    return position


def snake_and_ladder():
    global player1_pos
    global player2_pos
    global total_rolls
    global chance
    while player1_pos != 100 and player2_pos != 100:
        outcome = random.randint(1, 6)
        total_rolls += 1
        option = random.randint(1, 3)  # 1 - NoPlay, 2 - Ladder, 3 - Snake
        if chance == 1:
            player1_pos = update(player1_pos, option, outcome)
            if player1_pos == 100:  # Stop immediately if player 1 wins
                print(f"Player 1 Won after {total_rolls} rolls.")
                return
            chance = 2
        else:
            player2_pos = update(player2_pos, option, outcome)
            if player2_pos == 100:  # Stop immediately if player 2 wins
                print(f"Player 2 Won after {total_rolls} rolls.")
                return
            chance = 1

    if player1_pos == 100:
        print(f"Player 1 Won after {total_rolls} rolls.")
    else:
        print(f"Player 2 Won after {total_rolls} rolls.")


if __name__ == "__main__":
    snake_and_ladder()
