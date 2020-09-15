DAYS = 10


class CatalogItem:
    def __init__(self, itemId, title, tags):
        self._id = itemId
        self._title = title
        self._tags = tags

    @property
    def itemId(self):
        return self._id

    @property
    def title(self):
        return self._title

    def hasTag(self, arg):
        return arg in self._tags


class Scroll(CatalogItem):
    def __init__(self, itemId, title, tags, dateLastCleaned):
        super().__init__(itemId, title, tags)
        self._lastCleaned = dateLastCleaned

    def needCleaning(self, targetDate):
        threshold = 1500
        if self.hasTag("revered"):
            threshold = 700

        return self.daySinceLastCleaning(targetDate) > threshold

    def daySinceLastCleaning(self, targetDate):
        return self._lastCleaned.until(targetDate, DAYS)
