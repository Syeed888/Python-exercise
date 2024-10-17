seasons = ("winter", "spring", "summer", "autumn")

def get_seasons(month_number):
    if month_number in [12, 1, 2]:
        return seasons[0]
    elif month_number in [3, 4, 5]:
        return seasons[1]
    elif month_number in [6, 7, 8]:
        return seasons[2]
    elif month_number in [9, 10, 11]:
        return seasons[3]
    else:
        return "error"


long_seasons = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")

def get_seasons_2(month_number):
    if month_number > 12:
        return "error"
    return long_seasons[month_number - 1]

def get_value():
    return input("Enter month number: ")

month_str = get_value()
while month_str != "":
    print(get_seasons(int(month_str)))
    print(get_seasons_2(int(month_str)))
    month_str = get_value()