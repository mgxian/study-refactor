class Order:
    def __init__(self, data):
        self._priority = data.get('priority')

    @property
    def priority(self):
        return self._priority

    @property
    def priorityString(self):
        return self._priority.toString()

    @property.setter
    def priority(self, aString):
        self._priority = Priority(aString)


class Priority:
    def __init__(self, value):
        if len(filter(lambda v: v == value, Priority.legalValues())) > 0:
            this._value = value
        else:
            raise Exception("invalid priority value")

    def toString(self):
        return self._value

    @staticmethod
    def legalValues():
        return ['lower', 'normal', 'high', 'rush']

    @property
    def _index(self):
        return Priority.legalValues().index(self._value)

    def equals(self, other):
        return self._index == other._index

    def higherThan(self, other):
        return self._index > other._index

    def lowerThan(self, other):
        return self._index < other._index


orders = [Order({}), Order({})]
highPriorityCount = len(
    filter(lambda o: o.priority.higherThan(Priority('normal')), orders))
