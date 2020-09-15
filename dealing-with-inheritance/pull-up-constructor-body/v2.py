class Party:
    def __init__(self, name):
        self._name = name


class Employee(Party):
    def __init__(self, name, employeeId, monthlyCost):
        super(Party, self).__init__(name)
        self._id = employeeId
        self._monthlyCost = monthlyCost


class Department(Party):
    def __init__(self, name, staff):
        super(Party, self).__init__(name)
        self._staff = staff
