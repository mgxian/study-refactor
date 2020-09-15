class Booking:
    def __init__(self, show, date):
        self._show = show
        self._date = date
        self._premiumBookingDelegate = None

    def _bePremium(self, extras):
        self._premiumBookingDelegate = PremiumBookingDelegate(self, extras)

    @property
    def hasTalkback(self):
        if self._premiumBookingDelegate:
            return self._premiumBookingDelegate.hasTalkback()
        return self._show.hasOwnProperty('talkback') and not self.isPeakDay

    @property
    def basePrice(self):
        result = self._show.price
        if self.isPeakDay:
            result += round(result * 0.15)

        if self._premiumBookingDelegate:
            return self._premiumBookingDelegate.extendBasePrice(result)

        return result

    @property
    def hasDinner(self):
        if self._premiumBookingDelegate:
            return self._premiumBookingDelegate.hasDinner

        return None


class PremiumBookingDelegate:
    def __init__(self, hostBooking, extras):
        self._hostBooking = hostBooking
        self._extras = extras

    @property
    def hasTalkback(self):
        return self._hostBooking._show.hasOwnProperty('talkback')

    @property
    def extendBasePrice(self, result):
        return round(result+self._extras.premiumFee)

    @property
    def hasDinner(self):
        return self._extras.hasOwnProperty('dinner') and not self._hostBooking.isPeakDay


def createBooking(show, date):
    return Booking(show, date)


def createPremiumBooking(show, date, extras):
    result = Booking(show, date)
    result._bePremium(extras)
    return result


show = {}
date = {}
aBooking = createBooking(show, date)

extras = {}
aBooking = createPremiumBooking(show, date, extras)
