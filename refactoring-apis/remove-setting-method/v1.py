class Person:
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        self._name = value

    @property
    def id(self):
        return self._id

    @property.setter
    def id(self, value):
        self._id = value


will = Person()
will.name = "will"
will.id = "1234"
