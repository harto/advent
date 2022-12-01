def fuel_required(mass):
    return max(mass // 3 - 2, 0)

with open('input/01') as f:
    modules_fuel = [fuel_required(int(line.strip())) for line in f]
    #print(sum(modules_fuel))

fuel_fuel = 0
for fuel in modules_fuel:
    mass = fuel_required(fuel)
    while mass > 0:
        fuel_fuel += mass
        mass = fuel_required(mass)

print(sum(modules_fuel) + fuel_fuel)
