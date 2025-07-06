class Location:
    """
    Reprezentuje lokalizację geograficzną:
    - szerokość geograficzną (latitude)
    - długość geograficzną (longitude)
    - strefę czasową względem UTC (np. +1.0 dla CET, +2.0 dla CEST)
    """

    def __init__(self, latitude, longitude, tz_offset=0.0):
        self.latitude = latitude    # np. 51.94 (Zielona Góra)
        self.longitude = longitude  # np. 15.50
        self.tz_offset = tz_offset  # np. +1.0 dla CET

    def __repr__(self):
        return f"Location(lat={self.latitude}, lon={self.longitude}, tz={self.tz_offset:+})"
