def acquireData(input):
    lines = input.split("\n")
    loopItems = filter(lambda line: line.trim() != "", lines[1:])
    loopItems = map(lambda line: line.split(","), loopItems)
    loopItems = filter(lambda fields: fields[1].trim() == "India", loopItems)
    loopItems = map(lambda fields: {
                    'city': fields[0].trim(), 'phone': fields[2].trim()}, loopItems)
    return loopItems
