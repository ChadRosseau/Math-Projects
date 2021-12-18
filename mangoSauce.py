# To celebrate the holidays, Sam and Markus and 18 family members are seated at a circular table. 
# Everyone at the table would like to use some mango sauce, which happens to be in front of Sam at the moment.

# Instead of passing the sauce around in a circle, Sam passes it randomly to the person seated directly to their left or right. 
# They then do the same, passing it randomly either to the person to their left or right.

# This continues until everyone has, at some point, received the mango sauce.

# Of the 20 people in the circle, who has the greatest chance of being the last person to receive the mango sauce?

from random import randint

# Variables which might be interesting to edit
timesToRunSimulation = 1000
amountOfPeopleAtTable = 20

# Tracking Variables
totalPasses = 0
totalPassAverage = []

people = list(range(1, amountOfPeopleAtTable + 1))

class Person:

    def __init__(self, name):
        self.name = name
        self.count = 0

    def addLast(self):
        self.count += 1

peopleObjects = []
peopleObjects.append(Person("Sam"))
peopleObjects.append(Person("Markus"))

for i in range(3, len(people)+1):
    peopleObjects.append(Person("Person " + str(i)))

def core(people):
    for i in range(timesToRunSimulation):
        main(people)


    for people in peopleObjects:
        print(people.name + ": " + str(people.count) + " times, " + str(round(((people.count/timesToRunSimulation)*100), 2)) + "%")

    print("Total times mango sauce passed across all simulations: " + str(totalPasses))

def main(people):
    pos = 0
    passCount = 0
    mangoed = []
    while len(mangoed) < len(people):
        person = people[pos]
        # Uncomment line below to see the order of people who obtain the mango sauce ----------------------------------------
        # print(checkName(person))
        if person not in mangoed:
            mangoed.append(person)
        if len(mangoed) == len(people)-1:
            lastMangoed = recordName(mangoed)
        newPos = passSauce(pos)
        pos = newPos
        passCount += 1

    report(lastMangoed, passCount)


def passSauce(position):
    value = randint(1, 2)
    maxPos = len(people) - 1
    if value == 1:
        # Move position left
        newPos = position - 1
    elif value == 2:
        newPos = position + 1

    if newPos > maxPos:
        newPos = 0
    elif newPos < 0:
        newPos = maxPos

    return newPos


def checkName(name):
    if name == 1:
        return "Sam"
    elif name == 2:
        return "Markus"
    else:
        return ("Person " + str(name))

def recordName(mangoed):
    for person in people:
        if person not in mangoed:
            return checkName(person)


def report(lastMangoed, passCount):
    global totalPasses
    # Uncomment line below to see the name of the last person to get mango sauce each runthrough --------------------------------------
    # print("Last person to get mango sauce: " + lastMangoed)
    for person in peopleObjects:
        if person.name == lastMangoed:
            person.addLast()
    # Uncomment line below to see the amount of times the mango sauce was passed before everyone had had it each runthrough -----------
    #print("Times mango sauce was passed before everyone had mango sauce: " + str(passCount))
    totalPasses += passCount
    totalPassAverage.append(passCount)

for i in range(1):
    core(people)
    #print(i)

# newTotal = 0
# for i in range(len(totalPassAverage)):
#     newTotal = newTotal + totalPassAverage[i]
# print(newTotal/len(totalPassAverage))
# print(len(totalPassAverage))
