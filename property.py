import gameboard


rent_of_property = {"old kent road":{"state":1, "Prob":0.0225,"level1":70,"level2":130,"level3":220,"level4":370,"level5":750},
                    "whitechapel road":{"state":3, "Prob":0.0248,"level1":70,"level2":130,"level3":220,"level4":370,"level5":750},
                    "the angel islington":{"state":5, "Prob":0.0261,"level1":80,"level2":140,"level3":240,"level4":410,"level5":800},
                    "euston road":{"state":6, "Prob":0.0266,"level1":80,"level2":140,"level3":240,"level4":410,"level5":800},
                    "pentonyille":{"state":8, "Prob":0.0271,"level1":100,"level2":160,"level3":260,"level4":440,"level5":860},
                    "pall mall":{"state":10,"Prob":0.0267, "level1":110,"level2":180,"level3":290,"level4":460,"level5":900},
                    "whitehall":{"state":12,"Prob":0.0274, "level1":110,"level2":180,"level3":290,"level4":460,"level5":900},
                    "northhumb'nd avenue":{"state":13,"Prob":0.0278, "level1":130,"level2":200,"level3":310,"level4":490,"level5":980},
                    "bow street":{"state":14,"Prob":0.0292, "level1":140,"level2":210,"level3":330,"level4":520,"level5":1000},
                    "marlborough street":{"state":15,"Prob":0.0299, "level1":140,"level2":210,"level3":330,"level4":520,"level5":1000},
                    "vine street":{"state":17,"Prob":0.0303, "level1":160,"level2":230,"level3":350,"level4":550,"level5":1100},
                    "strand":{"state":19,"Prob":0.0297, "level1":170,"level2":250,"level3":380,"level4":580,"level5":1160},
                    "fleet street":{"state":21,"Prob":0.0288, "level1":170,"level2":250,"level3":380,"level4":580,"level5":1160},
                    "trafalgar square":{"state":22,"Prob":0.0283, "level1":190,"level2":270,"level3":400,"level4":610,"level5":1200},
                    "leicester square":{"state":23,"Prob":0.0286, "level1":200,"level2":280,"level3":420,"level4":640,"level5":1300},
                    "conventry street":{"state":24,"Prob":0.029, "level1":200,"level2":280,"level3":420,"level4":640,"level5":1300},
                    "piccadilly":{"state":26,"Prob":0.0289, "level1":220,"level2":300,"level3":440,"level4":670,"level5":1340},
                    "regent street":{"state":28,"Prob":0.0282, "level1":230,"level2":320,"level3":460,"level4":700,"level5":1400},
                    "oxford street":{"state":30,"Prob":0.0264, "level1":230,"level2":320,"level3":460,"level4":700,"level5":1400},
                    "bond street":{"state":31,"Prob":0.0254, "level1":250,"level2":340,"level3":480,"level4":730,"level5":1440},
                    "park lane":{"state":33,"Prob":0.0237, "level1":270,"level2":360,"level3":510,"level4":740,"level5":1500},
                    "mayfair":{"state":35,"Prob":0.0226, "level1":300,"level2":400,"level3":560,"level4":810,"level5":1600}
                    }


def upgrade_property(Player):
    
    property_name_1 = gameboard.game_board[Player.initial_state]["property"]["name"]
    
    if gameboard.game_board[Player.initial_state]["property"]["rent"] == rent_of_property[property_name_1]["level1"]:
        return rent_of_property[property_name_1]["level2"]
    elif gameboard.game_board[Player.initial_state]["property"]["rent"] == rent_of_property[property_name_1]["level2"]:
        return rent_of_property[property_name_1]["level3"]
    elif gameboard.game_board[Player.initial_state]["property"]["rent"] == rent_of_property[property_name_1]["level3"]:
        return rent_of_property[property_name_1]["level4"]
    elif gameboard.game_board[Player.initial_state]["property"]["rent"] == rent_of_property[property_name_1]["level4"]:
        return rent_of_property[property_name_1]["level5"]
    else:
        return rent_of_property[property_name_1]["level5"]
    