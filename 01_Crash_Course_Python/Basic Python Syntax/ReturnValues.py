def area_triangle(base, height):
    return base * height / 2

area_a = area_triangle(10, 6)
area_b = area_triangle(14, 10)

sum = area_a + area_b
print("The sum of the areas is:", sum)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(7000)
print(hours, minutes, seconds)

def convert_temp(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + 273.15
    reamur = celsius * 4 / 5
    return fahrenheit, kelvin, reamur

fahrenheit, kelvin,reamur = convert_temp(20)
print(fahrenheit, kelvin, reamur)

def find_total_days(years, months, days):
    my_days = (years * 365) + (months * 30) + days
    return my_days
print(find_total_days(3, 10, 2))