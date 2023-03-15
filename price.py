# dateStart
# dateEnd
# dish
# price
import datetime

class Price():
    def __init__(self, dateStart, dateEnd, dish, price):
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.dish = dish
        self.price = price

    def __init__(self, dateStart, dish, price):
        self.dateStart = dateStart
        self.dateEnd = datetime.date(3000, 12, 31)
        self.dish = dish
        self.price = price
