f = open("input.txt")
# print(f.read())
totalFuelRequirements = 0
def calc_Fuel(massAmount):
    return (int(mass) // 3) - 2 # this is totalFuelRequirement for inputted mass of fuel


while True:
    mass = f.readline()
    if not mass:
        break
    fuel = calc_Fuel(mass)
    while fuel > 0:
        totalFuelRequirements += fuel
        fuel = calc_Fuel(fuel)

f.close()
print("Total Fuel Requirements:", totalFuelRequirements)


# //this will round down automatically, you can't round up automatically
