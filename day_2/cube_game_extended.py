def deterime_cube_quantity(cubes):
    mult = 1

    for elem in cubes.values():
        mult *= int(elem)

    return mult

def determine_game_score(data):
    # Game 1: 19 blue, 12 red; 19 blue, 2 green, 1 red; 13 red, 11 blue
    f_data = data.lstrip("Game ")
    
    # Extracts the id
    id = f_data[0:f_data.find(":")]
    
    # Removes the characters up until ":" & remove all ","
    f_data = f_data[f_data.find(":") + 1:]
    f_data = f_data.replace(',', '')
    f_data = f_data.strip()

    sets = f_data.split(";")

    cubes = dict()

    for set in sets:
        set = set.strip().split(' ')
        set.reverse()

        idx = 0
        while (idx < len(set)):
            if set[idx] not in cubes.keys():
                cubes[set[idx]] = int(set[idx + 1])
                continue

            if int(cubes[set[idx]]) < int(set[idx + 1]):
                cubes[set[idx]] = int(set[idx + 1])
            
            idx += 2

    return deterime_cube_quantity(cubes)
    
def main():
    input_file = open('input.txt', 'r')
    data = input_file.readlines()

    # Todo
    sum = 0
    for line_data in data:
        sum += int(determine_game_score(line_data))

    print("The sum of the power of the games are " + str(sum) + '\n')

    input_file.close()

if __name__ == "__main__":
    main()