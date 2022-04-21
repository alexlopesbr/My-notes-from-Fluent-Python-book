# 03.03 | 96 | Dictcomps exemples

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]

country_code = {country.upper(): code for code, country in DIAL_CODES}
print(country_code)

code_country = {code: country for code, country in DIAL_CODES if code < 66}
print(code_country)
