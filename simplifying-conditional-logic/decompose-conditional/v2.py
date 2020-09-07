def totalChange(plan, aDate, quantity):
    if summer(plan, aDate):
        charge = summerChange(plan, quantity)
    else:
        charge = regularChange(plan, quantity)


def summer(plan, aDate):
    return (not aDate.isBefore(plan.summerStart)) and (not aDate.isAfter(plan.summerEnd))


def summerChange(plan, quantity):
    return quantity * plan.summerRate


def regularChange(plan, quantity):
    return quantity * plan.regularRate + plan.regularServiceCharge
