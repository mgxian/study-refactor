def payAmount(employee):
    result = 0
    if employee.isSeparated:
        return {"amount": 0, "reasonCode": "SEP"}
    if employee.isRetired:
        return {"amount": 0, "reasonCode": "RET"}
    # logic to compute amount
    return someFinalComputation()


def someFinalComputation():
    pass
