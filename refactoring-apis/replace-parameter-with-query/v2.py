class Order:
    @property
    def finalPrice(self):
        basePrice = self.quantity * self.itemPrice
        discountLevel = self.discountLevel
        return self.discountedPrice(basePrice, discountLevel)

    @property
    def discountLevel(self):
        return 2 if self.quantity > 100 else 1

    def discountedPrice(self, basePrice, discountLevel):
        if discountLevel == 1:
            return basePrice * 0.95
        elif discountLevel == 2:
            return basePrice * 0.9
