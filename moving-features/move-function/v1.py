class Account:
    def __init__(self, daysOverdrawn, accountType):
        self.daysOverdrawn = daysOverdrawn
        self.type = accountType

    @property
    def bankCharge(self):
        result = 4.5
        if self.daysOverdrawn > 0:
            result += self.overdraftCharge

        return result

    @property
    def overdraftCharge(self):
        if self.type.isPremium:
            baseCharge = 10
            if self.daysOverdrawn <= 7:
                return baseCharge
            else:
                return baseCharge+(self.daysOverdrawn-7)*0.85
        else:
            return self.daysOverdrawn * 1.75


class AccountType:
    def __init__(self, isPremium):
        self._isPremium = isPremium

    @property
    def isPremium(self):
        return self._isPremium
