def plumages(birds):
    return map(lambda bird: {"name": bird.name, "plumage": plumage(bird)}, birds)


def speeds(birds):
    return map(lambda bird: {"name": bird.name, "plumage": airSpeedVelocity(bird)}, birds)


def plumage(bird):
    if bird.type == 'EuropeanSwallow':
        return "average"
    elif bird.type == 'AfricanSwallow':
        return "tired" if bird.numberOfCoconuts > 2 else "average"
    elif bird.type == 'NorwegianBlueParrot':
        return "scorched" if bird.voltage > 100 else "beautiful"
    else:
        return "unknown"


def airSpeedVelocity(bird):
    if bird.type == 'EuropeanSwallow':
        return 35
    elif bird.type == 'AfricanSwallow':
        return 40 - 2 * bird.numberOfCoconuts
    elif bird.type == 'NorwegianBlueParrot':
        return 0 if bird.isNailed else 10 + bird.voltage / 10
    else:
        return None
