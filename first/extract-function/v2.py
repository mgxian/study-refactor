def printOwing(invoice):
    printBanner()
    outstanding = calculateOutstanding()

    printDetails(invoice, outstanding)


def printDetails(invoice, outstanding):
    print('name: {}'.format(invoice.customer))
    print('amount: {}'.format(outstanding))


def printBanner():
    pass


def calculateOutstanding():
    return 100
