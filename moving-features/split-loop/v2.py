import math


def main(people):
    return 'youngestAge: {}, totalSalary: {}'.format(youngestAge(), totalSalary())


def totalSalary(people):
    totalSalary = 0
    for p in people:
        totalSalary += p.salary
    return totalSalary


def youngestAge(people):
    youngest = people[0].age if people[0] else math.inf
    for p in people:
        if p.age < youngest:
            youngest = p.age
    return youngest
