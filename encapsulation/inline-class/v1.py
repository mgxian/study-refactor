class TrackingInformation:
    def __init__(self, shippingCompany, trackingNumber):
        self._shippingCompany = shippingCompany
        self._trackingNumber = trackingNumber

    @property
    def shippingCompany(self):
        return self._shippingCompany

    @property.setter
    def shippingCompany(self, arg):
        self._shippingCompany = arg

    @property
    def trackingNumber(self):
        return self._trackingNumber

    @property.setter
    def settrackingNumber(self, arg):
        self._trackingNumber = arg

    @property
    def display(self):
        return '{}: {}'.format(self.shippingCompany, self.trackingNumber)


class Shipment:
    def __init__(self, shippingCompany, trackingNumber):
        self._trackingInfomation = TrackingInformation(
            shippingCompany, trackingNumber)

    @property
    def trackingInfo(self):
        return self._trackingInfomation.display

    @property
    def trackingInformation(self):
        return self._trackingInfomation

    @property.setter
    def trackingInformation(self, arg):
        self._trackingInfomation = arg


aShipment = Shipment()
aShipment.trackingInformation.shippingCompany = 'will'
