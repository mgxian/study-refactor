class Site:
    @property
    def customer(self):
        if self._customer == 'unknown':
            return UnknownCustomer()
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


class UnknownCustomer:
    @property
    def isUnknown(self):
        return True

    @property
    def name(self):
        return 'occupant'

    @property
    def paymentHistory(self):
        return NullPaymentHistory()


class NullPaymentHistory:
    @property
    def weeksDelinquentInLastYear(self):
        return 0


def isUnknown(arg):
    if not (isinstance(arg, Customer) or isinstance(arg, UnknownCustomer)):
        raise Exception('bad value {}'.format(arg))
    return arg.isUnknown


aSite = Site()
aCustomer = aSite.customer
customerName = aCustomer.name


weeksDelinquent = aCustomer.paymentHistory.weeksDelinquentInLastYear
