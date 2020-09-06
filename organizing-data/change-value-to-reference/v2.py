class Order:
    def __init__(self, data):
        self._number = data.get('number')
        self._customer = registerCustomer(data.get('customer'))

    @property
    def customer(self):
        return self._customer


class Customer:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


_repositoryData = {}
_repositoryData['customers'] = {}


def registerCustomer(id):
    if id not in _repositoryData['customers']:
        _repositoryData['customers'][id] = Customer(id)

    return findCustomer(id)


def findCustomer(id):
    return _repositoryData['customers'][id]
