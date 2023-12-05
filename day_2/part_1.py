import re

def find_valid_games(input_file):
    requirement = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    with open(input_file) as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            match = re.search(r'(Game (\d+): )', line)
            game = match.group(1)
            game_id = int(match.group(2))

            line = re.sub(game, "", line)
            sets = (line.strip()).split('; ')
            set_possible = []
            # iterate each set in one game
            for set in sets:
                revealed = set.split(', ')
                # iterate each colour and number revealed in the set
                for num_colour in revealed:
                    revealed_match = re.search(r'(\d+) (red|green|blue)', num_colour)
                    num = int(revealed_match.group(1))
                    colour = revealed_match.group(2)
                    # if requirement is met, append True, else append False
                    if requirement.get(colour) >= num:
                        set_possible.append(True)
                    else:
                        set_possible.append(False)
            # if there is one False, then the entire Game is not possible
            if all(set_possible):
                sum += game_id
        print(f'The sum of the IDs of games that are possible is: {sum}')


if __name__ == "__main__":
    find_valid_games("adventofcode.com_2023_day_2_input.txt")