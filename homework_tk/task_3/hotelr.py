class Hotel:
    def __init__(self, fullname, age, money, country, day_h, phone):
        self.fullname = fullname
        self.age = age
        self.money = money
        self.country = country
        self.day_h = day_h
        self.phone = phone

    def get_hotel(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "age": self.age,
                "money": self.money,
                "country": self.country,
                "day_h": self.day_h,
                "phone": self.phone
            }
        return [
            self.fullname,
            self.age,
            self.money,
            self.country,
            self.day_h,
            self.phone
        ]
