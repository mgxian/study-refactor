organization = {
    "name": "Acme Gooseberries",
    "country": "GB"
}


def getRawDataOfOrganization():
    return organization


name = getRawDataOfOrganization().get("name")
getRawDataOfOrganization()['name'] = name
