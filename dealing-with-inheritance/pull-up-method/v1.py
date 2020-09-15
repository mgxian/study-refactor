class Party:
    pass


class Employee(Party):
    @property
    def annualCost(self):
        return self.monthlyCost * 12


class Department(Party):
    @property
    def totalAnnualCost(self):
        return self.monthlyCost * 12
