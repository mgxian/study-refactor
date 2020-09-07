def plumages(birds):
    return map(lambda bird: {"name": bird.name, "plumage": plumage(bird)}, birds)


def speeds(birds):
    return map(lambda bird: {"name": bird.name, "plumage": airSpeedVelocity(bird)}, birds)


def plumage(bird):
    return Bird(bird).plumage


def airSpeedVelocity(bird):
    return Bird(bird).airSpeedVelocity


class Bird:
    def __init__(self, birdObject):
        self.type = birdObject.type
        self.voltage = birdObject.voltage
        self.numberOfCoconuts = birdObject.numberOfCoconuts
        self.isNailed = birdObject.isNailed

    @property
    def plumage(self):
        if self.type == 'EuropeanSwallow':
            return "average"
        elif self.type == 'AfricanSwallow':
            return "tired" if self.numberOfCoconuts > 2 else "average"
        elif self.type == 'NorwegianBlueParrot':
            return "scorched" if self.voltage > 100 else "beautiful"
        else:
            return "unknown"

    @property
    def airSpeedVelocity(self):
        if self.type == 'EuropeanSwallow':
            return 35
        elif self.type == 'AfricanSwallow':
            return 40 - 2 * self.numberOfCoconuts
        elif self.type == 'NorwegianBlueParrot':
            return 0 if self.isNailed else 10 + self.voltage / 10
        else:
            return None
