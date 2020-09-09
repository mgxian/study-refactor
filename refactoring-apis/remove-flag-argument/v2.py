def rushDeliveryDate(anOrder):
    deliveryTime = 0
    if anOrder.deliveryState in ["MA", "CT"]:
        deliveryTime = 1
    elif anOrder.deliveryState in ["NY", "NH"]:
        deliveryTime = 2
    else:
        deliveryTime = 3
    return anOrder.placedOn.plusDays(1 + deliveryTime)


def regularDeliveryDate(anOrder):
    deliveryTime = 0
    if anOrder.deliveryState in ["MA", "CT", "NY"]:
        deliveryTime = 2
    elif anOrder.deliveryState in ["ME", "NH"]:
        deliveryTime = 3
    else:
        deliveryTime = 4
    return anOrder.placedOn.plusDays(2 + deliveryTime)


anOrder = {}
deliveryDate = rushDeliveryDate(anOrder)


deliveryDate = regularDeliveryDate(anOrder)
