def foundPerson(people):
    candidates = ["Don", "John", "Kent"]
    for person in people:
        if person in candidates:
            return person
