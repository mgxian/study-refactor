class Order:
    def __init__(self, quantity, item):
        self._quantity = quantity
        self._item = item

    @property
    def price(self):
        basePrice = self._quantity * self._item.price
        discountFactor = 0.98
        if basePrice > 1000:
            discountFactor -= 0.03

        return basePrice * discountFactor
