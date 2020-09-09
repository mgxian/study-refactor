class Employee:
    def __init__(self, name, typeCode):
        self._name = name
        self._typeCode = typeCode

    @property
    def name(self):
        return self._name

    @property
    def typeCode(self):
        return self._typeCode

    @staticmethod
    @property
    def legalTypeCode():
        return {
            "E": "Engineer",
            "M": "Manager",
            "S": "Salesman"
        }


name = 'will'
typeCode = 'E'
candidate = Employee(name, typeCode)


leadEngineerName = 'mgxian'
leadEngineer = Employee(leadEngineerName, 'E')
