import random

class Armor_and_Health:
    def __init__(self, image, name, max_Health: int = 500, max_Armor: int = 500):
        self.max_Health = max_Health
        self.current_Health = max_Health
        self.max_Armor = max_Armor
        self.current_Armor = max_Armor
        self.name = name
        self.image = image
    
    # String Return
    def __str__(self):
        return f"Health: {self.current_Health}/{self.max_Health} \n Armor: {self.current_Armor}/{self.max_Armor}"
    
    # Getters and Setters
    @property
    def current_Health(self):
        return self._current_Health
    
    @current_Health.setter
    def current_Health(self, value: int): 
        if(value < 0):
            self._current_Health = 0
        elif(value >= 0):
            self._current_Health = value
    
    @property
    def max_Health(self):
        return self._max_Health
    
    @max_Health.setter
    def max_Health(self, value: int):
            self._max_Health = value
    
    @property
    def current_Armor(self):
        return self._current_Armor
    
    @current_Armor.setter
    def current_Armor(self, value: int): 
        if(value < 0):
            self._current_Armor = 0
        elif(value >= 0):
            self._current_Armor = value
    
    @property
    def max_Armor(self):
        return self._max_Armor
    
    @max_Armor.setter
    def max_Armor(self, value: int):
        self._max_Armor = value
    
    # Healing Functions
        # The rand variable tells the function if the healing is set or random in a set range
    def Heal(self, value: int = 25, rand: bool = False):
        current_health = self.current_Health
        lower_Value = value - 10
        rand_num = ((random.randint(lower_Value,value)) + 20)
        if (rand == False)and current_health < self.max_Health:
            self.current_Health = current_health + value
        elif (rand == True) and self.current_Health < self.max_Health:
            self.current_Health += rand_num
    
    def Repair(self, value: int = 25, rand: bool = False):
        current_Armor = self.current_Armor
        lower_Value = value - 10
        rand_num = ((random.randint(lower_Value,value)) + 20)
        if (rand == False) and self.current_Armor < self.max_Armor:
            self.current_Armor = current_Armor + value
        elif (rand == True) and self.current_Armor < self.max_Armor:
            self.current_Armor +=  rand_num
    
    # Damaging Functions
        # The rand variable tells the function if the damage is set or random in a set range
    def damage_Health(self, value: int = 25, rand: bool = False):
        current_health = self.current_Health
        lower_Value = value - 10
        rand_num = ((random.randint(lower_Value,value)) + 20)
        if (rand == False):
            self.current_Health = current_health - value
        elif (rand == True):
            self.current_Health = current_health - rand_num
    
    def damage_Armor(self, value: int = 25, rand: bool = False):
        current_Armor = self.current_Armor
        lower_Value = value - 10
        rand_num = ((random.randint(lower_Value,value)) + 20)
        if (rand == False):
            self.current_Armor = current_Armor - value
        elif (rand == True):
            self.current_Armor = current_Armor - rand_num


class Moves(Armor_and_Health):
    def __init__(self, move_Name: str = "Move", Hit_Rate: int = 60, Power: int = 25, Move_Damage_Type: bool = False):
        self.Move_Name = move_Name
        self.Move_Hit_Rate = Hit_Rate
        self.Move_Power = Power
        self.Move_Damage_Type = Move_Damage_Type
        self.success = False

    # String Return
    def __str__(self):
        return f"{self.Move_Name}:\n\tHit Rate: {self.Move_Hit_Rate}%\n\tPowrer: {self.Move_Power}\n\tDamage Type: {self.Move_Damage_Type}"
    
    # Getters and Setters
    @property
    def Move_Name(self):
        return self._Move_Name
    
    @Move_Name.setter
    def Move_Name(self, value: str):
        length = len(value)
        if(length <= 0):
            self._Move_Name = "Move"
        elif(length > 0):
            self._Move_Name = value
    
    @property
    def Move_Hit_Rate(self):
        return self._Move_Hit_Rate
    
    @Move_Hit_Rate.setter
    def Move_Hit_Rate(self, value: int):
        if (value <= 100 and value > 0):
            self._Move_Hit_Rate = value
        else:
            self._Move_Hit_Rate = 60
    
    @property
    def Move_Power(self):
        return self._Move_Power
    
    @Move_Power.setter
    def Move_Power(self, value: int):
        if (value < 25 and value > 500):
            self._Move_Power = 25
        elif (value >= 25 and value <= 500):
            self._Move_Power = value
    
    @property
    def Move_Damage_Type(self):
        return self._Move_Damage_Type
    
    @Move_Damage_Type.setter
    def Move_Damage_Type(self, value: bool):
        self._Move_Damage_Type = value

    # Functions to use a move.
        # The rand variable takes a true\false value to determine if the move does random or fixed healing\damage
    def use_Attack_Move(self, enemy, rand: bool = False):
        damage = self.Move_Power
        damage_Type = self.Move_Damage_Type
        accuracy = self.Move_Hit_Rate
        rand_num = random.randint(1,101)
        if (rand_num <= accuracy):
            opp_A = enemy.current_Armor
            crit = damage*2
            if (opp_A <= 0):
                if (damage_Type == False):
                    enemy.damage_Health(crit, rand)
                elif (damage_Type == True):
                    enemy.damage_Health( damage, rand)
                self.success = True
            elif (opp_A > 0):
                if (damage_Type == False):
                    enemy.damage_Armor(damage, rand)
                elif (damage_Type == True):
                    enemy.damage_Armor(crit, rand)
                self.success = True
        else:
            print("Miss")
            self.success = False
        
    def use_Repair_Move(self, target, rand: bool = False):
        power = self.Move_Power
        target.Repair(power, rand)
    
    def use_Heal_Move(self, target, rand: bool = False):
        power = self.Move_Power
        target.Heal(power, rand)        



#### test ####


P1 = Armor_and_Health("images\\player.png", "The Player")

B1 = Moves("Lasers", 80, 50, True)
B2 = Moves("Machine Guns", 50, 80, False)
B3 = Moves("Basic Repair", 90, 50, True)
B4 = Moves("Basic Heal", 90, 50, False)

OB1 = Moves("Lasers", 70, 30, True)
OB2 = Moves("Machine Guns", 30, 70, False)
OB3 = Moves("Basic Repair", 90, 50, True)
OB4 = Moves("Basic Heal", 90, 50, False)


player_moves_list = [B1, B2, B3, B4]
opponent_moves_list = [OB1, OB2, OB3, OB4]
