WEAPONS = ['R', 'P', 'S']

class WrongNumberOfPlayerError(Exception):
    def __str__(self):
        return "Игроков должно быть 2"
    

class NoSuchStrategyError(Exception):
    def __str__(self):
        return "Игрок сделал ход не R, P или S"
    

def check_players_value(player_1, player_2) -> str:
    if player_1[1] == 'P' and player_2[1] == 'R':
        return f"{player_1[0]} P"
    elif player_1[1] == 'R' and player_2[1] == 'S':
        return f"{player_1[0]} R"
    elif player_1[1] == 'S' and player_2[1] == 'P':
        return f"{player_1[0]} S"
    else:
        if player_1[1] == player_2[1]:
            return "Ничья"
        
        if not (player_1[1] in WEAPONS):
            raise NoSuchStrategyError()
        
        if not (player_2[1] in WEAPONS):
            raise NoSuchStrategyError()
        
        return f"{player_2[0]} {player_2[1]}"



def rps_game_winner(value = []):
    if (len(value) >= 3) or (len(value) <= 0):
        raise WrongNumberOfPlayerError()
    
    for player_step in value:
        if isinstance(player_step, list) == False:
            raise Exception("Вложенный элемент списка не является типом list")
        
    # выявление победителя
    player_1 = value[0]
    player_2 = value[1]

    result = check_players_value(player_1, player_2)
    return result
    
print(rps_game_winner([["player1", 'P'], ["player2", "S"]]))
print(rps_game_winner([["player1", 'P'], ["player2", "A"]]))