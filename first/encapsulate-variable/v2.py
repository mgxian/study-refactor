from owner import getDefaultOwner, setDefaultOwner


def main():
    owner = getDefaultOwner()
    setDefaultOwner({"firstname": "will", "lastName": "mao"})
