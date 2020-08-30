class Shipment:
    def __init__(self, shippingCompany, trackingNumber):
        self._shippingCompany = shippingCompany
        self._trackingNumber = trackingNumber

    @property
    def trackingInfo(self):
        return '{}: {}'.format(self.shippingCompany, self.trackingNumber)

    @property
    def shippingCompany(self):
        return self.shippingCompany

    @property.setter
    def shippingCompany(self, arg):
        self.shippingCompany = arg

    @property
    def trackingNumber(self):
        return self.trackingNumber

    @property.setter
    def trackingNumber(self, arg):
        self.trackingNumber = arg


aShipment = Shipment()
aShipment.shippingCompany = 'will'
