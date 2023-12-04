import re

def parse_calibration(input_file):
    with open(input_file) as file:
        sum = 0
        lines = file.readlines()
        for line in lines:
            num_only = re.sub(r'[^\d]+', '', line)
            calibration_val = num_only[0] + num_only[-1]
            sum += int(calibration_val)
    print(f'The sum of calibrationvalue is: {sum}')


if __name__ == "__main__":
    parse_calibration("adventofcode.com_2023_day_1_input.txt")