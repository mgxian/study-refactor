class ChargeCalculator:
    def __init__(self, customer, usage, provider):
        self._customer = customer
        self._usage = usage
        self._provider = provider

    @property
    def baseCharge(self):
        return self._customer.baseRate * self._usage

    @property
    def charge(self):
        return self.baseCharge + self._provider.connectionCharge


customer = {}
usage = 10
provider = {}
monthCharge = ChargeCalculator(customer, usage, provider).charge
