class Site:
    @property
    def customer(self):
        return self._customer


class Customer:
    @property
    def name(self):
        return self._name

    @property
    def billingPlan(self):
        return self._billing_plan

    @property.setter
    def billingPlan(self, arg):
        self._billing_plan = arg

    @property
    def paymentHistory(self):
        return self._paymentHistory

    @property
    def isUnknown(self):
        return False


aSite = Site()
aCustomer = aSite.customer
if aCustomer == 'unknown':
    customerName = "occupant"
else:
    customerName = aCustomer.name


if aCustomer == "unknown":
    weeksDelinquent = 0
else:
    weeksDelinquent = aCustomer.paymentHistory.weeksDelinquentInLastYear
