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
    """Zwraca szczegółową pozycję Słońca jako słownik."""
    d = jd - 2451545.0
    L = normalize_angle(280.460 + 0.9856474 * d)
    M = normalize_angle(357.528 + 0.9856003 * d)
    lambda_sun = normalize_angle(L + 1.915 * sin_deg(M) + 0.020 * sin_deg(2 * M))

    sign_index = int(lambda_sun // 30)
    zodiac = ZODIAC_SIGNS[sign_index]
    degrees_in_sign = lambda_sun % 30

    return {
        "lon": lambda_sun,                    # np. 281.29
        "sign": zodiac,                       # np. "Koziorożec"
        "deg_in_sign": degrees_in_sign,       # np. 11.29
        "sign_index": sign_index              # 0 = Baran, 11 = Ryby
    }




def moon_position(jd):
    """Zwraca szczegółową pozycję Księżyca jako słownik."""
    d = jd - 2451545.0

    # Główne elementy
    L_moon = normalize_angle(218.316 + 13.176396 * d)
    M_moon = normalize_angle(134.963 + 13.064993 * d)
    M_sun = normalize_angle(357.529 + 0.9856003 * d)
    lambda_sun = sun_position(jd)["lon"]

    # Obliczenia długości ekliptycznej z poprawkami
    lambda_moon = L_moon \
        + 6.289 * sin_deg(M_moon) \
        + 1.274 * sin_deg(2 * (L_moon - lambda_sun) - M_moon) \
        + 0.658 * sin_deg(2 * (L_moon - lambda_sun)) \
        + 0.214 * sin_deg(2 * M_moon) \
        - 0.186 * sin_deg(M_sun)

    lambda_moon = normalize_angle(lambda_moon)

    # Opis znaku i stopni
    sign_index = int(lambda_moon // 30)
    zodiac = ZODIAC_SIGNS[sign_index]
    degrees_in_sign = lambda_moon % 30

    return {
        "lon": lambda_moon,
        "sign": zodiac,
        "deg_in_sign": degrees_in_sign,
        "sign_index": sign_index
    }



ZODIAC_SIGNS = [
    "Baran", "Byk", "Bliźnięta", "Rak", "Lew", "Panna",
    "Waga", "Skorpion", "Strzelec", "Koziorożec", "Wodnik", "Ryby"
]

def get_sign(degree):
    """Zwraca nazwę znaku zodiaku dla podanego kąta."""
    index = int(degree // 30) % 12
    return ZODIAC_SIGNS[index]
