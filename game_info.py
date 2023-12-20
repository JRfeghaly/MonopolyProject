from properties import *


class game_info:

    def __init__(self, game_number):
        properties_list = []

        self.game_number = game_number
        starting_line = 32 * (game_number - 1)
        ending_line = starting_line + 31

        with open("in.txt", 'r') as file:
            all_lines = file.readlines()
            game_list = all_lines[starting_line: ending_line - 3]

        for i in range(len(game_list)):
            temp = game_list[i][:-1].split()
            game_list[i] = temp

        for line in game_list:

            case_number = int(line[0])
            case_type = line[1][0]
            case_type_number = int(line[1][1])
            case_name = line[1][line[1].find("_"):]
            houses = int(line[2])
            is_mortgaged = int(line[3])

            if len(line) == 5:
                properties_list.append(
                    properties(case_number, case_type, case_type_number, case_name, houses, is_mortgaged, line[4]))
            else:
                properties_list.append(
                    properties(case_number, case_type, case_type_number, case_name, houses, is_mortgaged, ""))

        self.properties_list = properties_list

    def get_properties_list(self):
        return self.properties_list
