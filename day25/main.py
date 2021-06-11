# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas


def cel_to_fer(cel):
    return (cel / 5) * 9 + 32


data = pandas.read_csv('weather_data.csv')
# temp = data['temp'].tolist()
# print(f'The average of {temp} is {sum(temp) / len(temp)}')
# print(data['temp'].mean())
#
# print(data.condition)

monday = data[data.day == 'Monday']
print(f'On Monday the temp was {cel_to_fer(monday.temp)}')

print(data[data.temp == data.temp.max()])
