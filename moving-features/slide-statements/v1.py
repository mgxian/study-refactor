pricingPlan = retrievePricingPlan()
order = retreiveOrder()
baseCharge = pricingPlan.base
charge = 0
chargePerUnit = pricingPlan.unit
units = order.units
discount = 0
charge = baseCharge + units * chargePerUnit
discountableUnits = max(units - pricingPlan.discountThreshold, 0)
discount = discountableUnits * pricingPlan.discountFactor
if order.isRepeat:
    discount += 20
charge = charge - discount
chargeOrder(charge)


def retrievePricingPlan():
    pass


def retreiveOrder():
    pass


def chargeOrder(charge):
    pass
