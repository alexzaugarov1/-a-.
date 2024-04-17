import requests
from datetime import datetime, timedelta

# Введите свой ключ API
api_key = "YOUR_API_KEY"

def get_weather_data(start_date, end_date, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={start_date}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    sunny_days = 0
    total_wind_speed = 0
    count = 0

    for hour_data in data['hourly']:
        dt = hour_data['dt']
        date = datetime.fromtimestamp(dt).date()
        if start_date <= date <= end_date:
            count += 1
            if hour_data['weather'][0]['main'] == 'Clear':
                sunny_days += 1
            total_wind_speed += hour_data['wind_speed']

    avg_wind_speed = total_wind_speed / count if count else 0

    return sunny_days, avg_wind_speed

# Введите даты начала и конца в формате год-месяц-дата
start_date = datetime.strptime('2024-04-01', '%Y-%m-%d').date()
end_date = datetime.strptime('2024-04-10', '%Y-%m-%d').date()

# Введите координаты места
lat, lon = 55.75, 37.61  # Координаты города

sunny_days, avg_wind_speed = get_weather_data(start_date, end_date, lat, lon)


print(f"Количество солнечных дней: {sunny_days}")
print(f"Средняя скорость ветра: {avg_wind_speed}")

# Параметры
sunny_days = ... # Замените на количество солнечных дней
avg_wind_speed = ... # Замените на среднюю скорость ветра
A = ... # Замените на площадь, пересекаемую лопастями турбины
t = ... # Замените на время в секундах
P = ... # Замените на мощность солнечной панели
hours_of_sunlight = ... # Замените на количество часов солнечного света в день

# Плотность воздуха (около 1.225 кг/м³ на уровне моря)
rho = 1.225

# Переводим время из дней в секунды для первого случая
t_seconds = t * 24 * 60 * 60

# Расчет энергии для первого случая
E1 = 0.5 * rho * A * avg_wind_speed**3 * t_seconds

# Расчет энергии для второго случая
E2 = P * hours_of_sunlight * sunny_days

print(f"Количество энергии, выработанное в первом случае: {E1} джоулей")
print(f"Количество энергии, выработанное во втором случае: {E2} киловатт-часов")

cost_per_kwh = ... # Замените на стоимость электроэнергии за кВтч

# Переводим энергию из джоулей в киловатт-часы для первого случая
E1_kwh = E1 / (3.6 * 10**6)

# Расчет стоимости энергии для обоих случаев
cost1 = E1_kwh * cost_per_kwh
cost2 = E2 * cost_per_kwh

print(f"Стоимость энергии, выработанной в первом случае: {cost1} рублей")
print(f"Стоимость энергии, выработанной во втором случае: {cost2} рублей")