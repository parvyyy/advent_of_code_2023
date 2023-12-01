# Given a line of letters & numbers, find the calibration value.
# The calibration value can be found by combining the first digit and the last 
# digit (in that order) to form a single two-digit number.

# Your program must return the sum of all the calibration values.
def calc_calibration_value(line):
    value = ""
    for char in line:
        if char.isnumeric():
            value += char
            break

    for char in reversed(line):
        if char.isnumeric():
            value += char
            break

    return int(value)

def main():
    input_file = open('input.txt', 'r')
    data = input_file.readlines()

    sum = 0
    for line in data:
        sum += calc_calibration_value(line)

    print("The sum of all the calibration values is " + str(sum))

    input_file.close()

if __name__ == "__main__":
    main()