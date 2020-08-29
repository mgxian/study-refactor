def getRating(driver):
    return 2 if driver.numberOfLateDeliveries > 5 else 1
