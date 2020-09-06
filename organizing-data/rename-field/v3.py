organization = Organization({
    "name": "Acme Gooseberries",
    "country": "GB"
})


def getOrganization():
    return organization


class Organization:
    def __init__(self, data):
        self._data = data
        self._title = data.get("title")
        self._country = data.get("country")

    def rawDataOfOrganization(self):
        return self._data

    @property
    def title(self):
        return self._title

    @property.setter
    def title(self, value):
        self._title = value


name = getOrganization().title
getOrganization().name = name
