def distanceTravelled(scenario, time):
    result = 0
    primaryAcceleration = scenario.primaryForce / scenario.mass
    primaryTime = min(time, scenario.delay)
    result = 0.5 * primaryAcceleration * primaryTime * primaryTime
    secondaryTime = time - scenario.delay
    if secondaryTime > 0:
        primaryVelocity = primaryAcceleration * scenario.delay
        secondaryAcceleration = (
            scenario.primaryForce + scenario.secondaryForce) / scenario.mass
        result += primaryVelocity * secondaryTime + \
            0.5 * secondaryAcceleration * secondaryTime * secondaryTime

    return result
