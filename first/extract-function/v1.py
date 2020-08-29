def printOwing(invoice):
    printBanner()
    outstanding = calculateOutstanding()

    # print details
    print('name: {}'.format(invoice.customer))
    print('amount: {}'.format(outstanding))


def printBanner():
    pass


def calculateOutstanding():
    return 100
