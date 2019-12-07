def calculateFuel(mass):
    return int(mass/3) - 2


def showTotalMass():
    mass = open('input01.txt').readlines()
    totalMass = 0
    for i in mass:
        totalMass += calculateFuel(int(i))
    print(totalMass)


showTotalMass()
