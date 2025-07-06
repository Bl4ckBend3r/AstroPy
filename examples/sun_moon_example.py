from astro.sun_moon import julian_day, sun_position, moon_position

# Oblicz JD
jd = julian_day(2000, 1, 2, 9 + 37/60)

# Oblicz pozycje
sun = sun_position(jd)
moon = moon_position(jd)

# Wyświetlenie wyników
print(f"Słońce: {sun['lon']:.2f}° → {sun['deg_in_sign']:.2f}° {sun['sign']}")
print(f"Księżyc: {moon['lon']:.2f}° → {moon['deg_in_sign']:.2f}° {moon['sign']}")
