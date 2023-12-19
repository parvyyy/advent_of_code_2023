def is_valid_score(cubes):
    if 'red' in cubes and cubes['red'] > 12:
        return False
        
    if 'green' in cubes and cubes['green'] > 13:
        return False
    
    if 'blue' in cubes and cubes['blue'] > 14:
        return False
    
    return True

def determine_game_score(data):
    game_data = data.lstrip("Game ")
    
    # Extracts the id
    id = game_data[0 : game_data.find(":")]

    # Removes the characters up until ":"
    game_data = game_data[game_data.find(":") + 1 : ]
    game_data = game_data.replace(',', '').strip()

    indiv_game = game_data.split(';')

    cubes = dict()

    for game in indiv_game:
        game = game.strip().split(' ')
        game.reverse()

        idx = 0
        while (idx < len(game)):
            cubes[game[idx]] = int(game[idx + 1])
            idx += 2
        
        if not is_valid_score(cubes):
            return 0
        
        cubes.clear()

    return id
    
def main():
    input_file = open('input.txt', 'r')
    data = input_file.readlines()

    # Todo
    sum = 0
    for line_data in data:
        sum += int(determine_game_score(line_data))

    print("The sum of the IDs of the games are " + str(sum) + '\n')

    input_file.close()

if __name__ == "__main__":
    main()