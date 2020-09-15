class Employee:
    def __init__(self, name, typeCode):
        self.validateType(typeCode)
        self._name = name
        self._typeCode = typeCode

    def validateType(self, arg):
        if arg not in ["engineer", "manager", "salesman"]:
            raise Exception('Employee cannot be of type {}'.format(arg))

    def toString(self):
        return '{} ({})'.format(self._name, self._typeCode)
