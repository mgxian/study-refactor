class Order:
    def __init__(self, quantity, item):
        self._quantity = quantity
        self._item = item

    @property
    def price(self):
        return self.basePrice * self.discountFactor

    @property
    def basePrice(self):
        return self._quantity * self._item.price

    @property
    def discountFactor(self):
        discountFactor = 0.98
        if self.basePrice > 1000:
            discountFactor -= 0.03
        return discountFactor
