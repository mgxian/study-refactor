import math


def main(people):
    youngest = people[0].age if people[0] else math.inf
    totalSalary = 0
    for p in people:
        if p.age < youngest:
            youngest = p.age
        totalSalary += p.salary
    return 'youngestAge: {}, totalSalary: {}'.format(youngest, totalSalary)
