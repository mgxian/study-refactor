class Employee:
    def __init__(self, name, employeeId, monthlyCost):
        self._id = employeeId
        self._name = name
        self._monthlyCost = monthlyCost

    @property
    def monthlyCost(self):
        return self._monthlyCost

    @property
    def name(self):
        return self._name

    @property
    def employeeId(self):
        return self._id

    @property
    def annualCost(self):
        return self._monthlyCost*12


class Department:
    def __init__(self, name, staff):
        self._name = name
        self._staff = staff

    @property
    def staff(self):
        return self._staff

    @property
    def name(self):
        return self._name

    @property
    def totalMonthlyCost(self):
        pass

    @property
    def headCount(self):
        return len(self._staff)

    @property
    def totalAnnualCost(self):
        return self.totalMonthlyCost * 12
