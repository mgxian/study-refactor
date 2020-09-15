class Party:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def annualCost(self):
        return self.monthlyCost * 12


class Employee(Party):
    def __init__(self, name, employeeId, monthlyCost):
        super(Employee, self).__init__(name)
        self._id = employeeId
        self._monthlyCost = monthlyCost

    @property
    def monthlyCost(self):
        return self._monthlyCost

    @property
    def employeeId(self):
        return self._id


class Department(Party):
    def __init__(self, name, staff):
        super(Department, self).__init__(name)
        self._staff = staff

    @property
    def staff(self):
        return self._staff

    @property
    def monthlyCost(self):
        pass

    @property
    def headCount(self):
        return len(self._staff)
