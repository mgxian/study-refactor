class Booking:
    def __init__(self, show, date):
        self._show = show
        self._date = date

    @property
    def hasTalkback(self):
        return self._show.hasOwnProperty('talkback') and not self.isPeakDay

    @property
    def basePrice(self):
        result = self._show.price
        if self.isPeakDay:
            result += round(result * 0.15)
        return result


class PremiumBooking(Booking):
    def __init__(self, show, date, extras):
        super(PremiumBooking, self).__init__(show, date)
        self._extras = extras

    @property
    def hasTalkback(self):
        return self._show.hasOwnProperty('talkback')

    @property
    def basePrice(self):
        return round(super().basePrice + self._extras.premiumFee)

    @property
    def hasDinner(self):
        return self._extras.hasOwnProperty('dinner') and not self.isPeakDay


show = {}
date = {}
aBooking = Booking(show, date)

extras = {}
aBooking = PremiumBooking(show, date, extras)
