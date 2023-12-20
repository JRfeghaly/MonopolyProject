class player_info:

    def __init__(self, game_number):
        self.game_number = game_number
        starting_line = 32 * (game_number - 1)
        ending_line = starting_line + 31
        with open("in.txt", 'r') as file:

            all_lines = file.readlines()
            players_list = all_lines[ending_line - 3: ending_line + 1]

        for i in range(len(players_list)):
            temp = players_list[i][:-1].split()
            players_list[i] = temp

        money_per_player = {
        'A': int(players_list[0][1]),
        'B': int(players_list[1][1]),
        'C': int(players_list[2][1]),
        'D': int(players_list[3][1])
        }

        self.money_per_player = money_per_player

    def get_money_per_player(self):
        return self.money_per_player

    def get_game_number(self):
        return self.game_number