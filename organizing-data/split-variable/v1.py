def distanceTravelled(scenario, time):
    result = 0
    acc = scenario.primaryForce / scenario.mass
    primaryTime = min(time, scenario.delay)
    result = 0.5 * acc * primaryTime * primaryTime
    secondaryTime = time - scenario.delay
    if secondaryTime > 0:
        primaryVelocity = acc * scenario.delay
        acc = (scenario.primaryForce + scenario.secondaryForce) / scenario.mass
        result += primaryVelocity * secondaryTime + \
            0.5 * acc * secondaryTime * secondaryTime

    return result
