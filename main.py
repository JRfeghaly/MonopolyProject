from game_info import *
from player_info import *
from properties import *


def starting_money(game_number):
    property_prices = {
        'A1_Mediterraneal_Avenue': 60,
        'A2_Baltic_Avenue': 60,
        'B1_Oriental_Avenue': 100,
        'B2_Vermont_Avenue': 100,
        'B3_Connecticut_Avenue': 120,
        'C1_St.Charle\'s_Place': 140,
        'C2_States_Avenue': 140,
        'C3_Virginia_Avenue': 160,
        'D1_St.James_Place': 180,
        'D2_Tennessee_Avenue': 180,
        'D3_New_York_Avenue': 200,
        'E1_Kentucky_Avenue': 220,
        'E2_Indiana_Avenue': 220,
        'E3_Illinois_Avenue': 240,
        'F1_Atlantic_Avenue': 260,
        'F2_Ventinor_Avenue': 260,
        'F3_Martin_Gardens': 280,
        'G1_Pacific_Avenue': 300,
        'G2_North_Carolina_Avenue': 300,
        'G3_Pennsylvania_Avenue': 320,
        'H1_Park_Place': 350,
        'H2_Boardwalk': 400,
        'U1_Electric_Company': 150,
        'U2_Waterworks': 150,
        'R1_Reading_railroad': 200,
        'R2_Pennsylvania_Railroad': 200,
        'R3_BnO_Railroad': 200,
        'R4_Short_Line': 200
    }
    upgrade_costs = {
        'A1_Mediterraneal_Avenue': 50,
        'A2_Baltic_Avenue': 50,
        'B1_Oriental_Avenue': 100,
        'B2_Vermont_Avenue': 100,
        'B3_Connecticut_Avenue': 50,
        'C1_St.Charle\'s_Place': 100,
        'C2_States_Avenue': 100,
        'C3_Virginia_Avenue': 100,
        'D1_St.James_Place': 150,
        'D2_Tennessee_Avenue': 150,
        'D3_New_York_Avenue': 150,
        'E1_Kentucky_Avenue': 150,
        'E2_Indiana_Avenue': 150,
        'E3_Illinois_Avenue': 150,
        'F1_Atlantic_Avenue': 150,
        'F2_Ventinor_Avenue': 150,
        'F3_Martin_Gardens': 150,
        'G1_Pacific_Avenue': 200,
        'G2_North_Carolina_Avenue': 200,
        'G3_Pennsylvania_Avenue': 200,
        'H1_Park_Place': 200,
        'H2_Boardwalk': 200,
    }

    players = player_info(game_number)
    money = players.get_money_per_player()
    game_temp = game_info(game_number)
    game = game_temp.get_properties_list()

    for prop in game:
        owner = prop.get_owner()
        name = prop.get_case_name()
        full_name = prop.get_full_name()
        case_type = prop.get_case_type()
        houses = prop.get_houses()
        if owner != '':
            money[owner] += property_prices[full_name]

            if case_type not in 'UR':
                money[owner] += int(houses) * upgrade_costs[full_name]

            if prop.get_is_mortgaged() == 1:
                money[owner] -= property_prices[full_name] / 2

    return round((money['A'] + money['B'] + money['C'] + money['D']) / 4)


def overall_averages():
    f = open("monopoly/out.txt", "w")
    string_result = ''

    for i in range(1, 1001):
        string_result += str(starting_money(i)) + '\n'

    f.write(string_result[:-1])
    f.close()
