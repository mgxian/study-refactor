def renderPerson(outStream, person):
    result = []
    result.append('<p>{}</p>'.format(person.name))
    result.append(emitPhotoData(person.photo))
    return "\n".join(result)


def photoDiv(p):
    return "\n".join([
        "<div>",
        emitPhotoData(p),
        "</div>",
    ])


def emitPhotoData(p):
    return '\n'.join(['<p>title: {}</p>'.format(p.title),
                      '<p>location: {}</p>'.format(p.location),
                      '<p>date: {}</p>'.format(p.date.toDateString())
                      ])
