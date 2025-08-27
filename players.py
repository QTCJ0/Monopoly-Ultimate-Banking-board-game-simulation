from dataclasses import dataclass
import gameboard
import property
import secrets

num_of_win = {"player1":0,"player2":0,"player3":0,"player4":0}
times_step_on_property = [0]*36
countround = 0
list_player1 = []
list_player2 = []
list_player3 = []
list_player4 = []
list_ini_p1 = []
list_ini_p2 = []
list_ini_p3 = []
list_ini_p4 = []
for x in range(10000):
    list_of_property_owned = [1,3,5,6,8,10,12,13,14,15,17,19,21,22,23,24,26,28,30,31,33,35]
    property_on_board = gameboard.game_board

    class Player():
        
        def __init__(self):
            self.initial_fund: int = 1500
            self.initial_state: int = 0
            self.num_of_property: int = 0
            self.list_of_property: list = []

    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()


    #查看房地产是否被拥有
    def property_is_ownned(name):
        for a in player1.list_of_property:
            if  name == a:
                return 1
        for b in player2.list_of_property: 
            if  name == b:
                return 1
        for c in player3.list_of_property:
            if name == c:
                return 1
        for d in player4.list_of_property:
            if  name == d:
                return 1
        return 0
        
    #查看具体是谁拥有这块地
    def check_owner_of_property(name):
        for a in player1.list_of_property:
            if  name == a:
                return player1
        for b in player2.list_of_property: 
            if  name == b:
                return player2
        for c in player3.list_of_property:
            if name == c:
                return player3
        for d in player4.list_of_property:
            if  name == d:
                return player4

    #决定赢家
    def winner(f1, f2, f3, f4):
        list_of_fund = [f1, f2, f3, f4]
        max_ele = max(list_of_fund)
        if(max_ele == player1.initial_fund):
            return "player1"
        if(max_ele == player2.initial_fund):
            return "player2"
        if(max_ele == player3.initial_fund):
            return "player3"
        if(max_ele == player4.initial_fund):
            return "player4"

    #Row two dice
    def row_a_dice():
        steps = 0
        dice1 = secrets.randbelow(6)+1
        dice2 = secrets.randbelow(6)+1
        steps += (dice1 + dice2)
        if dice1 == dice2:
            return 1, steps
        else:
            return 0,steps

    def which_property_state_bigger(Player):
        max1 = 0
        for y in Player.list_of_property:
            
            if property.rent_of_property[y]["state"]>max1:
                
                max1 = property.rent_of_property[y]["state"]
                
        return max1

    def teleport(Player,state):
        index = 0
        if len(list_of_property_owned) != 0:
            for y in list_of_property_owned:
                if y>=state:
                    index += y
                    break
                elif y<state:
                    Player.initial_fund+=200
                    index += y
                    break
        elif len(list_of_property_owned) == 0:
            if len(Player.list_of_property) == 0:
                index += state 
            else:
                index +=which_property_state_bigger(Player)
            
        return index

    #玩家可能的行动
    def players_action(Player):
        countloop = 1
        flag = 1

        while flag and countloop<3:
            wether_row_a_double, step = row_a_dice()
            flag = wether_row_a_double
            countloop+=1
            Player.initial_state += step
                
            if Player.initial_state > 35:
                Player.initial_fund += 200
                Player.initial_state -= 36
                    
            times_step_on_property[Player.initial_state]+=1
                
            if Player.initial_state == 0 or Player.initial_state == 2 or Player.initial_state == 7 or Player.initial_state == 4 or Player.initial_state == 9 or \
            Player.initial_state == 11 or Player.initial_state == 16 or Player.initial_state == 18 or Player.initial_state == 25 or Player.initial_state == 20 or \
            Player.initial_state == 29 or Player.initial_state == 34 or Player.initial_state == 32:
                continue
                
            elif Player.initial_state == 27:
                Player.initial_state = 9
                times_step_on_property[9]+=1
                continue
    
            else:    
                property_price = property_on_board[Player.initial_state]["property"]["price"]
                property_rent = property_on_board[Player.initial_state]["property"]["rent"]
                property_name = property_on_board[Player.initial_state]["property"]["name"]
                    # 有米买地
                if (Player.initial_fund > property_price) and (1 - property_is_ownned(property_name)):
                    
                    #没有主人的土地购买后减去房地产的钱
                    Player.initial_fund -= property_price
                        
                    #没有主人的土地购买后添加到P1的propert list中
                    Player.list_of_property.append(property_name)
                    
                    list_of_property_owned.remove(Player.initial_state)
                    
                    continue
                    
                    #有米到他人的房产爆金币付租金
                elif (Player.initial_fund >= property_rent) and property_is_ownned(property_name):
                        
                    #查看房屋拥有者
                    owner_of_house = check_owner_of_property(property_name)
                        
                    #是自己的房子，房租升一级
                    if Player == owner_of_house:
                            
                        property_rent = property.upgrade_property(Player)
                        
                        continue
                            
                    else:
                            
                        #P1爆金币
                        Player.initial_fund -= property_rent
                            
                        #Pn获得钱
                        owner_of_house.initial_fund += property_rent
                            
                        property_rent = property.upgrade_property(Player)
                            
                        continue
                        
                elif (Player.initial_fund) < property_rent and property_is_ownned(property_name):
                    #查看房屋拥有者
                    owner_of_house = check_owner_of_property(property_name)
                        
                    if  Player == owner_of_house:
                            
                        property_rent = property.upgrade_property(Player)
                            
                        continue
                        
                    elif Player != owner_of_house:
                            
                        Player.initial_fund -= property_rent
                        
                        owner_of_house.initial_fund += property_rent
                            
                        return 0
                        
                elif (Player.initial_fund < property_rent) and (1 - property_is_ownned(property_name)):
                        
                    continue
                    
                else:
                    return 0
        else:
            if flag==0 and countloop<3:
                return 1
            else:
                Player.initial_state==9
                Player.initial_fund-=50
                return 1
     
    #Activation part
    for i in range(50):
        
        if players_action(player1):
            # print("player1 在"+str(player1.initial_state))
            # print("player1 有"+str(player1.list_of_property))
            # print("player1 left:"+str(player1.initial_fund))
            # pass
            countround+=1
            pass
        else:
            # print("player1 在"+str(player1.initial_state))
            # print("player1 goes broke")
            
            break
            
        if players_action(player2):
            # print("player2 在"+str(player2.initial_state))
            # print("player2 有"+str(player2.list_of_property))
            # print("player2 left:"+str(player2.initial_fund))
            pass
            
        else:
            # print("player2 在"+str(player2.initial_state))
            # print("player2 goes broke")
        
            break
            
        if players_action(player3):
            # print("player3 在"+str(player3.initial_state))
            # print("player3 有"+str(player3.list_of_property))
            # print("player3 left:"+str(player3.initial_fund))
            pass
        else:
            # print("player3 在"+str(player3.initial_state))
            # print("player3 goes broke")
       
            break
            
        if players_action(player4):
            # print("player4 在"+str(player4.initial_state))
            # print("player4 有"+str(player4.list_of_property))
            # print("player4 left:"+str(player4.initial_fund))
            pass
        else:
            # print("player4 在"+str(player4.initial_state))
            # print("player4 goes broke")
            
            break

    
    #Determine winner    
    winn = winner(player1.initial_fund, player2.initial_fund, player3.initial_fund, player4.initial_fund)
    
    
    if winn=="player1":
        num_of_win["player1"]+=1
        list_player1.append(len(player1.list_of_property))
        list_player2.append(len(player2.list_of_property))
        list_player3.append(len(player3.list_of_property))
        list_player4.append(len(player4.list_of_property))
        list_ini_p1.append(player1.initial_fund)
        list_ini_p2.append(player2.initial_fund)
        list_ini_p3.append(player3.initial_fund)
        list_ini_p4.append(player4.initial_fund)
        
    if winn=="player2":
        num_of_win["player2"]+=1
        list_player1.append(len(player1.list_of_property))
        list_player2.append(len(player2.list_of_property))
        list_player3.append(len(player3.list_of_property))
        list_player4.append(len(player4.list_of_property))
        list_ini_p1.append(player1.initial_fund)
        list_ini_p2.append(player2.initial_fund)
        list_ini_p3.append(player3.initial_fund)
        list_ini_p4.append(player4.initial_fund)
    if winn=="player3":
        num_of_win["player3"]+=1
        list_player1.append(len(player1.list_of_property))
        list_player2.append(len(player2.list_of_property))
        list_player3.append(len(player3.list_of_property))
        list_player4.append(len(player4.list_of_property))
        list_ini_p1.append(player1.initial_fund)
        list_ini_p2.append(player2.initial_fund)
        list_ini_p3.append(player3.initial_fund)
        list_ini_p4.append(player4.initial_fund)
    if winn=="player4":
        num_of_win["player4"]+=1
        list_player1.append(len(player1.list_of_property))
        list_player2.append(len(player2.list_of_property))
        list_player3.append(len(player3.list_of_property))
        list_player4.append(len(player4.list_of_property))
        list_ini_p1.append(player1.initial_fund)
        list_ini_p2.append(player2.initial_fund)
        list_ini_p3.append(player3.initial_fund)
        list_ini_p4.append(player4.initial_fund)
        
# print("player1 wins:"+str(num_of_win["player1"]))

# print("player2 wins:"+str(num_of_win["player2"]))

# print("player3 wins:"+str(num_of_win["player3"]))

# print("player4 wins:"+str(num_of_win["player4"]))

#During 10000 times of playing monopoly, number of times players step on each block.
print(times_step_on_property)
print(sum(times_step_on_property))
# count total rounds of the 10000 times of playing monopoly
print(countround)

# sum_of_init = sum(list_ini_p1)
# print(sum_of_init/10000)
# sum_of_init = sum(list_ini_p2)
# print(sum_of_init/10000)
# sum_of_init = sum(list_ini_p3)
# print(sum_of_init/10000)
# sum_of_init = sum(list_ini_p4)
# print(sum_of_init/10000)