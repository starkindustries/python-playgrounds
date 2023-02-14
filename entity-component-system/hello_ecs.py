# Entity Component System Python Demo
class Entity(object):
    pass


class Plant():
    def __init__(self):
        self.requirements = ["water", "minerals"]
        self.growth = None
        self.name = "plant"
        self.seeds = []

    def reproduce(self):
        seed = Plant()
        seed.growth = Growth()
        seed.position = (self.position[0] + 1, self.position[1] + 1)
        self.seeds.append(seed)
        return seed

class Growth:
    def __init__(self):
        self.size = 0

class World:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def get_entities_at_position(self, position):
        return [entity for entity in self.entities if entity.position == position]

    def growth_system(self):
        growth_entities = []
        for e in self.entities:
            if hasattr(e, "growth"):
                growth_entities.append(e)

        for entity in growth_entities:
            nearby_entities = self.get_entities_at_position(entity.position)
            if all(req in [e.name for e in nearby_entities] for req in entity.requirements):
                entity.growth.size += 1
                if entity.growth.size % 5 == 0:
                    seed = entity.reproduce()
                    self.entities.append(seed)



# Create a new Plant instance
# Create a new Growth instance and add it to the Plant instance
plant1 = Plant()
plant1.growth = Growth()
plant1.position = (0, 0)

# Create a new World instance
world = World()
# Add the Plant instance to the World
world.add_entity(plant1)

# Create a "water" and "minerals" entity and add them to the world
water = Entity()
water.name = "water"
water.position = (0, 0)

minerals = Entity()
minerals.name = "minerals"
minerals.position = (0, 0)

world.add_entity(water)
world.add_entity(minerals)

for i in range(10):
    print(f"********** {i} **********")
    world.growth_system()
    print("plant1 size:", plant1.growth.size)  # Output: 0    
    for entity in world.entities:
        print(f"{entity.position}: {entity.name}")