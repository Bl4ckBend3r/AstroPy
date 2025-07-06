from astro.location import Location
from astro.utils import get_jd_from_local
from astro.sun_moon import sun_position, moon_position
from astro.planets import planet_position

# Zielona Góra, 10:37 lokalnego czasu CET (UTC+1)
loc = Location(51.94, 15.50, tz_offset=+1.0)
hour_local = 10 + 37/60

jd = get_jd_from_local(2000, 1, 2, hour_local, loc)

# Pozycje
sun = sun_position(jd)
moon = moon_position(jd)
mercury = planet_position(jd, "Mercury")

def show(obj, name):
    print(f"{name}: {obj['lon']:.2f}° → {obj['deg_in_sign']:.2f}° {obj['sign']}")

show(sun, "Słońce")
show(moon, "Księżyc")
show(mercury, "Merkury")
