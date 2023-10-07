import random
from vessels import Vessels, SupportCraft, OffensiveCraft

fleet_lenght = 50
grid_length = 100  # The given grid max of 100*100

# Let's create the fleet, a mixed up between support and offensive
fleets = []
for fleet in range(fleet_lenght):
    pass


# We need to find out the type different type ships that are close to each other and paur them


def distance_between_ships(ship1, ship2):
    return abs(ship1["x"] - ship2["x"]) + abs(ship1["y"] - ship2["y"])


# pairs the ships

pairs = []
