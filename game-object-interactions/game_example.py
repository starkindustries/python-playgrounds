import json

class GameObject:
    def __init__(self, name):
        self.name = name

    def interact(self, other):
        with open("interactions.json") as file:
            interactions = json.load(file)["interactions"]
            for interaction in interactions:
                if interaction["object1"] == self.name and interaction["object2"] == other.name:
                    getattr(self, interaction["method"])(other)
                elif interaction["object2"] == self.name and interaction["object1"] == other.name:
                    getattr(other, interaction["method"])(self)

class Tree(GameObject):
    def __init__(self, height):
        super().__init__("Tree")
        self.height = height

    def cut_down(self):
        self.height = 0

class Axe(GameObject):
    def __init__(self):
        super().__init__("Axe")

    def cut(self, tree):
        tree.cut_down()

class Water(GameObject):
    def __init__(self, amount):
        super().__init__("Water")
        self.amount = amount

class WaterCan(GameObject):
    def __init__(self, capacity):
        super().__init__("WaterCan")
        self.capacity = capacity
        self.amount = 0

    def fill(self, water):
        self.amount = min(self.capacity, self.amount + water.amount)
        water.amount = max(water.amount - self.capacity, 0)
        
# test code
tree = Tree(10)
axe = Axe()
tree.interact(axe)
print(tree.height) # 0

water = Water(5)
watercan = WaterCan(3)
watercan.interact(water)
print(watercan.amount) # 3
print(water.amount) # 2
