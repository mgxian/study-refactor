def baseCharge(usage):
    if usage < 0:
        return usd(0)

    amount = bottomBand(usage) * 0.03 + middleBand(usage) * \
        0.05 + topBand(usage) * 0.07
    return usd(amount)


def bottomBand(usage):
    return min(usage, 100)


def middleBand(usage):
    if usage > 100:
        return min(usage, 200) - 100
    else:
        return 0


def topBand(usage):
    if usage > 200:
        return usage - 200
    else:
        return 0


def usd(aNumber):
    pass
