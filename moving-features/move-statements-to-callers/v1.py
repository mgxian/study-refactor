def renderPerson(outStream, person):
    outStream.write('<p>{}</p>\n'.format(person.name))
    emitPhotoData(outStream, person.photo)


def listRecentPhotos(outStream, photos):
    photos = filter(lambda p: p.date > recentDateCutoff(), photos)
    for p in photos:
        outStream.write("<div>\n")
        emitPhotoData(outStream, p)
        outStream.write("</div>\n")


def recentDateCutoff():
    pass


def emitPhotoData(outStream, photo):
    outStream.write('<p>title: {}</p>\n'.format(photo.title))
    outStream.write('<p>date: {}</p>\n'.format(photo.date.toDateString()))
    outStream.write('<p>location: {}</p>\n'.format(photo.location))
