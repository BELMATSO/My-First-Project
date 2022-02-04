import random


def show_table(row_list):
    table = "" \
            " ________ \n" \
            "/        \\\n" \
            f"|{''.join(row_list[0])}|\n" \
            f"|{''.join(row_list[1])}|\n" \
            f"|{''.join(row_list[2])}|\n" \
            f"|{''.join(row_list[3])}|\n" \
            f"|{''.join(row_list[4])}|\n" \
            f"|{''.join(row_list[5])}|\n" \
            f"|{''.join(row_list[6])}|\n" \
            f"|{''.join(row_list[7])}|\n" \
            f"\\        /\n" \
            "----------\n"
    print(table)


def throw_ball(lis):
    while True:
        # Create a dice simulator
        dice = [me.randint(0, 7) for i in range(2)]  # Creating a list of dice generated randomly
        row = dice[0]
        column = dice[1]
        print(dice)
        if dice not in lis:
            lis.append(dice)
            print(lis)
            table_rows[row][column] = "0"
            show_table(table_rows)
            table_rows[row][column] = " "
            break


me = random.Random()  # Creating an object instance of the Class 'random'

table_rows = [
    [' ', ' ', 'O', 'O', 'O', 'O', ' ', ' '],
    [' ', ' ', 'O', 'O', 'O', ' ', ' ', ' '],
    [' ', ' ', 'O', 'O', ' ', ' ', ' ', ' '],
    [' ', ' ', 'O', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]
show_table(table_rows)
count = 0
guess_list = []
for r in table_rows:
    while "O" in r:
        throw_ball(guess_list)
        count += 1
print(count)

