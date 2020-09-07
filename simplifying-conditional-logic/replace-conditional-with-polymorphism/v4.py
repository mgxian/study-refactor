def plumages(birds):
    return map(lambda bird: {"name": bird.name, "plumage": createBird(bird).plumage}, birds)


def speeds(birds):
    return map(lambda bird: {"name": bird.name, "plumage": createBird(bird).airSpeedVelocity}, birds)


class Bird:
    def __init__(self, birdObject):
        self.type = birdObject.type
        self.voltage = birdObject.voltage
        self.numberOfCoconuts = birdObject.numberOfCoconuts
        self.isNailed = birdObject.isNailed

    @property
    def plumage(self):
        return "unknown"

    @property
    def airSpeedVelocity(self):
        return None


class EuropeanSwallow(Bird):
    @property
    def plumage(self):
        return "average"

    @property
    def airSpeedVelocity(self):
        return 35


class AfricanSwallow(Bird):
    @property
    def plumage(self):
        return "tired" if self.numberOfCoconuts > 2 else "average"

    @property
    def airSpeedVelocity(self):
        return 40 - 2 * self.numberOfCoconuts


class NorwegianBlueParrot(Bird):
    @property
    def plumage(self):
        return "scorched" if self.voltage > 100 else "beautiful"

    @property
    def airSpeedVelocity(self):
        return 0 if self.isNailed else 10 + self.voltage / 10


def createBird(bird):
    if bird.type == 'EuropeanSwallow':
        return EuropeanSwallow()
    elif bird.type == 'AfricanSwallow':
        return AfricanSwallow()
    elif bird.type == 'NorwegianBlueParrot':
        return NorwegianBlueParrot()
    else:
        return Bird()
