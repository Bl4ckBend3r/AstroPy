from astro.sun_moon import julian_day, sun_position, moon_position, get_sign

# Obliczenia czasu
jd = julian_day(2000, 1, 2, 9 + 37/60)

# Pozycje
sun_lon = sun_position(jd)
moon_lon = moon_position(jd)

# Wynik
print(f"Słońce: {sun_lon:.2f}° → {get_sign(sun_lon)}")
print(f"Księżyc: {moon_lon:.2f}° → {get_sign(moon_lon)}")
