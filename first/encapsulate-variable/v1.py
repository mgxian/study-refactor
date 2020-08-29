defaultOwner = {"firstname": "Martin", "lastName": "Fowler"}


def main():
    global defaultOwner
    owner = defaultOwner
    defaultOwner = {"firstname": "will", "lastName": "mao"}


main()
