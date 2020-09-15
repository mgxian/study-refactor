class Party:
    @property
    def annualCost(self):
        return self.monthlyCost * 12

    @property
    def monthlyCost(self):
        raise Exception("Subclass responsibility error")


class Employee(Party):
    @property
    def monthlyCost(self):
        return 1


class Department(Party):
    @property
    def monthlyCost(self):
        return 10
