import re
import numpy

def find_valid_games(input_file):
    with open(input_file) as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            match = re.search(r'(Game (\d+): )', line)
            game = match.group(1)
            line = re.sub(game, "", line)
            sets = (line.strip()).split('; ')

            # stores the largest number of cube of that colour
            largest_num_cube = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            power = 0
            # iterate each set in one game
            for set in sets:
                revealed = set.split(', ')
                # iterate each colour and number revealed in the set
                for num_colour in revealed:
                    revealed_match = re.search(r'(\d+) (red|green|blue)', num_colour)
                    num = int(revealed_match.group(1))
                    colour = revealed_match.group(2)
                    # if the current number of cube of the colour is larger than the previous one, update it
                    if num > largest_num_cube[colour]:
                        largest_num_cube[colour] = num

            power = numpy.prod(list(largest_num_cube.values()))
            sum += power

        print(f'The sum of the IDs of games that are possible is: {sum}')


if __name__ == "__main__":
    find_valid_games("adventofcode.com_2023_day_2_input.txt")