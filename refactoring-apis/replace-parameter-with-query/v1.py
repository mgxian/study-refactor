class Order:
    @property
    def finalPrice(self):
        basePrice = self.quantity * self.itemPrice
        discountLevel = 0
        if (self.quantity > 100):
            discountLevel = 2
        else:
            discountLevel = 1

        return self.discountedPrice(basePrice, discountLevel)

    def discountedPrice(self, basePrice, discountLevel):
        if discountLevel == 1:
            return basePrice * 0.95
        elif discountLevel == 2:
            return basePrice * 0.9
