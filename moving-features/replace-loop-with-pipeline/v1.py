def acquireData(input):
    lines = input.split("\n")
    firstLine = True
    result = []
    for line in lines:
        if firstLine:
            firstLine = False
            continue

        if line.trim() == "":
            continue

        record = line.split(",")
        if record[1].trim() == "India":
            result.push({'city': record[0].trim(), 'phone': record[2].trim()})

    return result
