def disabilityAmount(anEmployee):
    if isNotEligibleForDisability(anEmployee):
        return 0


def isNotEligibleForDisability(anEmployee):
    return anEmployee.seniority < 2 or anEmployee.monthsDisabled > 12 or anEmployee.isPartTime
