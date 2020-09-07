def totalChange(plan, aDate, quantity):
    if not aDate.isBefore(plan.summerStart) and not aDate.isAfter(plan.summerEnd):
        charge = quantity * plan.summerRate
    else:
        charge = quantity * plan.regularRate + plan.regularServiceCharge
