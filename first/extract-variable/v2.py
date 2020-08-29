def price(order):
    # price is base price - quantity discount + shipping
    basePrice = order.quantity*order.itemPrice
    quantityDiscount = max(0, order.quantity-500) * order.itemPrice*0.05
    shipping = min(basePrice*0.1, 100)
    return basePrice - quantityDiscount + shipping
