def priceOrder(product, quantity, shippingMethod):
    basePrice = product.basePrice * quantity
    discount = max(quantity - product.discountThreshold, 0) * \
        product.basePrice * product.discountRate
    shippingPerCase = shippingMethod.discountedFee if basePrice > shippingMethod.discountThreshold else shippingMethod.feePerCase
    shippingCost = quantity * shippingPerCase
    price = basePrice - discount + shippingCost
    return price
