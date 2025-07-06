import math
from datetime import datetime



def julian_day(year, month, day, hour=0.0):
    """Oblicza Julian Day z daty gregoriańskiej."""
    if month <= 2:
        year -= 1
        month += 12
    A = math.floor(year / 100)
    B = 2 - A + math.floor(A / 4)
    jd = math.floor(365.25 * (year + 4716)) \
         + math.floor(30.6001 * (month + 1)) \
         + day + hour / 24.0 + B - 1524.5
    return jd

def sin_deg(x): return math.sin(math.radians(x))
def cos_deg(x): return math.cos(math.radians(x))
def normalize_angle(deg): return deg % 360



def sun_position(jd):
    """Zwraca długość ekliptyczną Słońca dla danego JD."""
    d = jd - 2451545.0  # dni od J2000.0

    # Średnia długość geocentryczna Słońca (L)
    L = normalize_angle(280.460 + 0.9856474 * d)

    # Średnia anomalia Słońca (M)
    M = normalize_angle(357.528 + 0.9856003 * d)

    # Równanie środka
    lambda_sun = L + 1.915 * sin_deg(M) + 0.020 * sin_deg(2 * M)
    return normalize_angle(lambda_sun)



def moon_position(jd):
    """Zwraca długość ekliptyczną Księżyca dla danego JD."""
    d = jd - 2451545.0

    # Średnia długość Księżyca
    L_moon = normalize_angle(218.316 + 13.176396 * d)

    # Średnia anomalia Księżyca
    M_moon = normalize_angle(134.963 + 13.064993 * d)

    # Średnia anomalia Słońca
    M_sun = normalize_angle(357.529 + 0.9856003 * d)

    # Długość ekliptyczna Księżyca (z poprawkami)
    lambda_moon = L_moon \
        + 6.289 * sin_deg(M_moon) \
        + 1.274 * sin_deg(2 * (L_moon - sun_position(jd)) - M_moon) \
        + 0.658 * sin_deg(2 * (L_moon - sun_position(jd))) \
        + 0.214 * sin_deg(2 * M_moon) \
        - 0.186 * sin_deg(M_sun)
    
    return normalize_angle(lambda_moon)

ZODIAC_SIGNS = [
    "Baran", "Byk", "Bliźnięta", "Rak", "Lew", "Panna",
    "Waga", "Skorpion", "Strzelec", "Koziorożec", "Wodnik", "Ryby"
]

def get_sign(degree):
    """Zwraca nazwę znaku zodiaku dla podanego kąta."""
    index = int(degree // 30) % 12
    return ZODIAC_SIGNS[index]
