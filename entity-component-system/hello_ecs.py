# Entity Component System Python Demo

class Entity(object):
    pass


class Plant():
    def __init__(self):
        self.requirements = ["water", "minerals"]
        self.growth = None
        self.name = "plant"


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
        
        print(growth_entities)
        for entity in growth_entities:
            nearby_entities = self.get_entities_at_position(entity.position)
            if all(req in [e.name for e in nearby_entities] for req in entity.requirements):
                entity.growth.size += 1


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

# Run the growth system
world.growth_system()

# Print the size of the Plant
print("plant1:", plant1.growth.size)  # Output: 1

# Run the growth system again
world.growth_system()

# Print the size of the Plant
print("plant1:", plant1.growth.size)  # Output: 2
