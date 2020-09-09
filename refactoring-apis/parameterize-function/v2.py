import math


def baseCharge(usage):
    if usage < 0:
        return usd(0)

    amount = withinBand(usage, 0, 100) * 0.03 + withinBand(usage, 100, 200) * \
        0.05 + withinBand(usage, 200, math.inf) * 0.07
    return usd(amount)


def withinBand(usage, bottom, top):
    if usage > bottom:
        return min(usage, top) - bottom
    else:
        return 0


def usd(aNumber):
    pass
