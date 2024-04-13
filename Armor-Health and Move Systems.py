import random

class Armor_and_Health:
    def __init__(self, max_Health = 500, max_Armor = 500):
        self.max_Health = max_Health
        self.current_Health = max_Health
        self.max_Armor = max_Armor
        self.current_Armor = max_Armor
    
    def __str__(self):
        return f"Health: {self.current_Health}/{self.max_Health} \n Armor: {self.current_Armor}/{self.max_Armor}"
    
    @property
    def current_Health(self):
        return self._current_Health
    
    @current_Health.setter
    def current_Health(self, value): 
        if(value < 0):
            self._current_Health = 0
        elif(value >= 0):
            self._current_Health = value
    
    @property
    def max_Health(self):
        return self._max_Health
    
    @max_Health.setter
    def max_Health(self, value):
        if(value <= 500):
            self._max_Health = 500
        else:
            self._max_Health = value
    
    @property
    def current_Armor(self):
        return self._current_Armor
    
    @current_Armor.setter
    def current_Armor(self, value): 
        if(value < 0):
            self._current_Armor = 0
        elif(value >= 0):
            self._current_Armor = value
    
    @property
    def max_Armor(self):
        return self._max_Armor
    
    @max_Armor.setter
    def max_Armor(self, value):
        if(value <= 500):
            self._max_Armor = 500
        else:
            self._max_Armor = value
    
    def Heal(self, value = 25, rand = False):
        current_health = self.current_Health
        rand_num = ((random.randint(1,value)) + 20)
        if (rand == False):
            self.current_Health = current_health + value
        elif (rand == True):
            self.current_Health = current_health + rand_num
    
    def Repair(self, value = 25, rand = False):
        current_Armor = self.current_Armor
        rand_num = ((random.randint(1,value)) + 20)
        if (rand == False):
            self.current_Armor = current_Armor + value
        elif (rand == True):
            self.current_Armor = current_Armor + rand_num
    
    def damage_Health(self, value = 25, rand = False):
        current_health = self.current_Health
        rand_num = ((random.randint(1,value)) + 20)
        if (rand == False):
            self.current_Health = current_health - value
        elif (rand == True):
            self.current_Health = current_health - rand_num
    
    def damage_Armor(self, value = 25, rand = False):
        current_Armor = self.current_Armor
        rand_num = ((random.randint(1,value)) + 20)
        if (rand == False):
            self.current_Armor = current_Armor - value
        elif (rand == True):
            self.current_Armor = current_Armor - rand_num


class Moves(Armor_and_Health):
    def __init__(self, Name = "Move", Hit_Rate = 60, Power = 25, Damage_Type = False):
        self.Move_Name = Name
        self.Move_Hit_Rate = Hit_Rate
        self.Move_Power = Power
        if (Damage_Type == False):
            self.Move_Damage_Type = "Physical"
        elif (Damage_Type == True):
            self.Move_Damage_Type = "Energy"

    def __str__(self):
        return f"{self.Move_Name}:\n\tHit Rate: {self.Move_Hit_Rate}%\n\tPowrer: {self.Move_Power}\n\tDamage Type: {self.Move_Damage_Type}"
    
    @property
    def Move_Name(self):
        return self._Move_Name
    
    @Move_Name.setter
    def Move_Name(self, value):
        length = len(value)
        if(length <= 0):
            self._Move_Name = "Move"
        elif(length > 0):
            self._Move_Name = value
    
    @property
    def Move_Hit_Rate(self):
        return self._Move_Hit_Rate
    
    @Move_Hit_Rate.setter
    def Move_Hit_Rate(self, value):
        if (value <= 100 and value > 0):
            self._Move_Hit_Rate = value
        else:
            self._Move_Hit_Rate = 60
    
    @property
    def Move_Power(self):
        return self._Move_Power
    
    @Move_Power.setter
    def Move_Power(self, value):
        if (value < 25 and value > 500):
            self._Move_Power = 25
        elif (value >= 25 and value <= 500):
            self._Move_Power = value
    
    @property
    def Move_Damage_Type(self):
        return self._Move_Damage_Type
    
    @Move_Damage_Type.setter
    def Move_Damage_Type(self, bol = False):
        if (bol == False):
            self._Move_Damage_Type = "Physical"
        elif (bol == True):
            self._Move_Damage_Type = "Energy"




P1 = Armor_and_Health()
print(P1)
P1.damage_Health()
P1.damage_Armor(34, True)
print(P1)