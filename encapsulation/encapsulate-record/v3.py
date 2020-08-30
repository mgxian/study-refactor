organization = Organization({
    "name": "Acme Gooseberries",
    "country": "GB"
})


def getOrganization():
    return organization


class Organization:
    def __init__(self, data):
        self._data = data
        self._name = data.get("name")
        self._country = data.get("country")

    def rawDataOfOrganization(self):
        return self._data

    @property
    def name(self):
        return self._name

    @property.setter
    def name(self, value):
        self._name = value


name = getOrganization().name
getOrganization().name = name
