import re

def parse_calibration(input_file):
    numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    with open(input_file) as file:
        sum = 0
        lines = file.readlines()
        for line in lines:
            regex = re.compile(r'(\d)|(?=(one))|(?=(two))|(?=(three))|(?=(four))|(?=(five))|(?=(six))|(?=(seven))|(?=(eight))|(?=(nine))')
            matches = regex.findall(line)
            # keep only non empty capturing groups, not matches
            groups = [group for group in zip(*matches) if any(group)]
            result = []
            # compile a result list that contains only digits
            for group in zip(*groups):
                for digit in group:
                    if digit:
                        if digit in numbers_dict:
                            result.append(numbers_dict.get(digit)) 
                        else:
                            result.append(digit) 
            calibration_val = result[0] + result[-1]
            sum += int(calibration_val)
    print(f'The sum of calibrationvalue is: {sum}')

if __name__ == "__main__":
    parse_calibration("adventofcode.com_2023_day_1_input.txt")