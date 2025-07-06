class Chart:
    def __init__(self, date, time, lat, lon, tz='+00:00'):
        self.date = date
        self.time = time
        self.lat = lat
        self.lon = lon
        self.tz = tz
        self.planets = {}
        self.houses = {}
        self.aspects = []

    def calculate(self):
        # Tu będzie wywołanie efemeryd i domów
        pass
