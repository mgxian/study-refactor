def charge(customer, usage, provider):
    baseCharge = customer.baseRate * usage
    return baseCharge + provider.connectionCharge


customer = {}
usage = 10
provider = {}
monthCharge = charge()
