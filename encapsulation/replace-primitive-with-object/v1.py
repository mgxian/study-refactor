class Order:
    def __init__(self, data):
        self.priority = data.get('priority')


orders = [Order({}), Order({})]
filter(lambda o: o.priority == 'high' or o.priority == 'rush', orders)
