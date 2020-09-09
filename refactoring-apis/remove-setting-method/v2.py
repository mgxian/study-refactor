class Person:
    def __init__(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        self._name = value

    @property
    def id(self):
        return self._id


will = Person("1234")
will.name = "will"
