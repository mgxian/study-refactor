class Account:
    def __init__(self, daysOverdrawn, accountType):
        self.daysOverdrawn = daysOverdrawn
        self.type = accountType

    @property
    def bankCharge(self):
        result = 4.5
        if self.daysOverdrawn > 0:
            result += self.type.overdraftCharge(self.daysOverdrawn)

        return result


class AccountType:
    def __init__(self, isPremium):
        self._isPremium = isPremium

    @property
    def isPremium(self):
        return self._isPremium

    def overdraftCharge(self, daysOverdrawn):
        if self.isPremium:
            baseCharge = 10
            if daysOverdrawn <= 7:
                return baseCharge
            else:
                return baseCharge+(daysOverdrawn-7)*0.85
        else:
            return daysOverdrawn * 1.75
