def priceOrder(product, quantity, shippingMethod):
    priceData = calculatePriceData()
    return applyShipping(priceData, shippingMethod)


def calculatePriceData(product, quantity):
    basePrice = product.basePrice * quantity
    discount = max(quantity - product.discountThreshold, 0) * \
        product.basePrice * product.discountRate
    priceData = {
        "basePrice": basePrice,
        "quantity": quantity,
        "discount": discount
    }
    return priceData


def applyShipping(priceData, shippingMethod):
    shippingPerCase = shippingMethod.discountedFee if priceData[
        "basePrice"] > shippingMethod.discountThreshold else shippingMethod.feePerCase
    shippingCost = priceData['quantity'] * shippingPerCase
    return priceData['basePrice'] - priceData['discount'] + shippingCost
