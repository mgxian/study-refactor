class Order:
    def __init__(self, data):
        self._number = data.get('number')
        self._customer = Customer(data.get('customer'))

    @property
    def customer(self):
        return self._customer


class Customer:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id
