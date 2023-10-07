class Vessels:
    def __int__(self, name, coordinates=(0, 0)):
        self.name = name
        self.coordinates = None

    def moveTowards(self, x, y):
        self.coordinates = (x, y)

    def __str__(self):
        return f"Vessel {self.name} is right at {self.coordinates} position"

# Now let's create 2 other vessels of different types
# Since we have already vessel created with common attributes, we are going inheritance approach


class SupportCraft(Vessels):
    def __int__(self, name, coordinates=(0, 0), type_of_vessel="support", medical_unit=True):
        super.__init__(name, coordinates)
        self.type_of_vessel = type_of_vessel
        self.medical_unit = medical_unit


class OffensiveCraft(Vessels):
    def __init__(self, name, coordinates=(0, 0), shields=False, type_of_vessel="offensive", canons_number=0):
        super.__init__(name, coordinates)
        self.shields = shields
        self.type_of_vessel = type_of_vessel
        self.canons_number = canons_number

    def shields_up(self):
        self.shields = True
        return f"Offensive shields are up for battle"


class CommandShip(OffensiveCraft):
    def __init__(self, name, coordinates=(0, 0), cannons=24):
        super().__init__(name, coordinates, "Command Ship", cannons)




