def renderPerson(outStream, person):
    result = []
    result.append('<p>{}</p>'.format(person.name))
    result.append('<p>title: {}</p>'.format(person.photo.title))
    result.append(emitPhotoData(person.photo))
    return "\n".join(result)


def photoDiv(p):
    return "\n".join([
        "<div>",
        '<p>title: {}</p>'.format(p.title),
        emitPhotoData(p),
        "</div>",
    ])


def emitPhotoData(aPhoto):
    result = []
    result.append('<p>location: {}</p>'.format(aPhoto.location))
    result.append('<p>date: {}</p>'.format(aPhoto.date.toDateString()))
    return "\n".join(result)
