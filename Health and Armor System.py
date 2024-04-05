import random

class Health:
    def __init__(self,max_Health = 500):
        self.max_Health = max_Health
        self.current_Health = max_Health
    
    def __str__(self):
        return f"Health: {self.current_Health}/{self.max_Health}"
    
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
    
    def random_Heal(self, value = 5):
        health = self.current_Health
        result = ((random.randint(1,value)) + 5)
        self.current_Health = health + result
    
    def set_Heal(self, value = 5):
        health = self.current_Health
        self.current_Health = health + value
    
    def random_Damage(self, value = 5):
        health = self.current_Health
        result = ((random.randint(1,value)) + 5)
        self.current_Health = health - result
    
    def set_Damage(self, value = 5):
        health = self.current_Health
        self.current_Health = health - value

class Armor:
    def __init__(self, max_Armor = 500):
        self.max_Armor = max_Armor
        self.current_Armor = max_Armor
    
    def __str__(self):
        return f"Armor: {self.current_Armor}/{self.max_Armor}"
    
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
    
    def random_Repair(self, value = 5):
        armor = self.current_Armor
        result = ((random.randint(1,value)) + 5)
        self.current_Armor = armor + result
    
    def set_Repair(self, value = 5):
        health = self.current_Health
        self.current_Health = health + value
    
    def random_Damage(self, value = 5):
        armor = self.current_Armor
        result = ((random.randint(1,value)) + 5)
        self.current_Armor = armor - result
    
    def set_Damage(self, value = 5):
        armor = self.current_Armor
        self.current_Armor = armor - value


H1 = Health()
A1 = Armor()

print(H1)
print(A1)

H1.random_Damage(10)
A1.random_Damage(10)

print(H1)
print(A1)