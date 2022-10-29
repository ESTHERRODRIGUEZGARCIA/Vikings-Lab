
# Soldier
import random
#hacer que los tests funcionen
class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength #should return the strength property of the Soldier
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage

# Viking


class Viking(Soldier): # new property, the name
    def __init__(self, name, health, strength):
        
        super().__init__(self, health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage."
        else:
            return f"{self.name} has died in act of combat."
    
    def battleCry(self):
        return f"Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A SAxon has received {damage} points of damage."
        elif self.health < 0:
            return f"A SAxon has died in act of combat."

# War


class War():
    #the armies should be empty
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result