def calculateFuel(mass):
    return int(mass/3) - 2


def showTotalMass():
    mass = open('input02.txt').readlines()
    totalMass = 0
    mass = [int(i) for i in mass]

    for i in mass:
        fuel = calculateFuel(i)
        morefuel = fuel
        count = fuel
        while(count > 0):
            count = calculateFuel(count)
            if count > 0:
                morefuel += count
        totalMass += morefuel
    print(totalMass)


showTotalMass()
