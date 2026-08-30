import requests

print("Welcome to the Weather App!")

a = input("Enter city name: ")

if a == "":
    print("City name cannot be empty!")
else:
    b = "YOUR_API_KEY"

    c = "https://api.openweathermap.org/data/2.5/weather"
    d = {
        "q": a,
        "appid": b,
        "units": "metric"
    }

    try:
        e = requests.get(c, params=d, timeout=10)

        if e.status_code == 200:
            f = e.json()

            temperature = f["main"]["temp"]
            humidity = f["main"]["humidity"]
            condition = f["weather"][0]["description"]
            wind = f["wind"]["speed"]

            print("\nWeather Information")
            print("City:", a)
            print("Temperature:", temperature, "°C")
            print("Temperature:", round((temperature * 9/5) + 32, 2), "°F")
            print("Humidity:", humidity, "%")
            print("Weather:", condition)
            print("Wind Speed:", wind, "m/s")

        elif e.status_code == 404:
            print("City not found!")
        elif e.status_code == 401:
            print("Invalid API key!")
        else:
            print("Something went wrong!")

    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.RequestException:
        print("Network error!")
