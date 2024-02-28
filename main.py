import csv
from convertor.temperature.temperature import (
    celsius_to_fahrenheit as cel,
    fahrenheit_to_celsius as fahr,
)
from convertor.distance.distance import (
    meters_to_feet as meters_f,
    feet_to_meters as feet_f
)


def convert_temperature(temperature, target_unit):

    if '°C' in temperature:
        celsius = int(temperature.strip('°C'))
        if target_unit == 'F':
            convert = cel(celsius)
        else:
            convert = celsius
    elif '°F' in temperature:
        fahrenheit = int(temperature.strip('°F'))
        if target_unit == 'C':
            convert = fahr(fahrenheit)
        else:
            convert = fahrenheit
    else:
        return "Invalid temperature format"

    return convert


def convert_distance(distance, target_unit):

    if 'm' in distance:
        meters = int(distance.strip('m'))
        if target_unit == 'ft':
            return meters_f(meters)
        else:
            return meters
    elif 'ft' in distance:
        feet = int(distance.strip('ft'))
        if target_unit == 'm':
            return feet_f(feet)
        else:
            return feet
    else:
        return "Invalid distance format"


def main(inputf, output, target_temp, target_dist):

    with open(inputf, encoding='UTF-8') as infile, open(output, 'w', encoding='UTF-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        headings = ['Date', 'Converted_distance', 'Converted_temperature']
        writer.writerow(headings)

        for row in reader:
            date = row['Date']
            distance = row['Distance']
            temperature = row['Reading']
            c_d = convert_distance(distance, target_dist)
            c_t = convert_temperature(temperature, target_temp)
            writer.writerow([date, f"{c_d:.0f}{target_dist}", f"{c_t:.0f}°{target_temp}"])


inputf = "temperature_data.csv"
output = "converted_temperature_data.csv"
target_temp = 'F'  # 'C' or 'F'
target_dist = 'ft'  # 'm' or 'ft'
main(inputf, output, target_temp, target_dist)
