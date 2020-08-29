def getRating(driver):
    return 2 if moreThanFiveLateDeliveries(driver) else 1


def moreThanFiveLateDeliveries(driver):
    return driver.numberOfLateDeliveries > 5
