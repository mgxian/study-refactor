class Party:
    pass


class Employee(Party):
    def __init__(self, name, employeeId, monthlyCost):
        super()
        self._id = employeeId
        self._name = name
        self._monthlyCost = monthlyCost


class Department(Party):
    def __init__(self, name, staff):
        super()
        self._name = name
        self._staff = staff
