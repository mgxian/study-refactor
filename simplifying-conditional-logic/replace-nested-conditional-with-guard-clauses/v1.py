def payAmount(employee):
    result = 0
    if employee.isSeparated:
        result = {"amount": 0, "reasonCode": "SEP"}
    else:
        if employee.isRetired:
            result = {"amount": 0, "reasonCode": "RET"}
        else:
            # logic to compute amount
            result = someFinalComputation()
    return result


def someFinalComputation():
    pass
