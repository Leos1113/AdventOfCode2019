def calculateFuel(mass):
    return int(mass/3) - 2


def showTotalMass():
    mass = open('./input01.txt').readlines()
    totalMass = 0
    mass = [int(i) for i in mass]

    for i in mass:
        totalMass += calculateFuel(i)
    print(totalMass)


showTotalMass()
