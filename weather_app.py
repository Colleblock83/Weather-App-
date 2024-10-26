#das soll mal nh wetter app werden na let's go 
import requests
get_url = "http://api.weatherapi.com/v1"

text1 = "Welcome to \033[1;35mWeatherZilla!\033[0m"
middle = text1.center(130)
print(middle)
hd2 = "Made by \033[33mColleblock83\033[0m"
middle2 = hd2.center(122)
print(middle2)
hd3 = "Donation on \033[34mPayPal\033[0m: @FabioBaensch"
middle3 = hd3.center(120)
print(middle3)
print()
print("\033[0;31m!WARNING!\033[0m: Dont forget to use Capital Letters so the program can work correctly!")
print()

choice = input("Please enter the name of the city or the post code: ")
while True:
    #Bekomme das wetter
    def get_weather():
        url = f"{get_url}/current.json" #Website mit API Daten

        dictionary = {
            "key" : "5fccdbadd4ae419dafa101938242610",  #Mein API Key
            "q" : choice,                             #Postleitzahl, Koordinaten oder Stadt
        }

        get_data = requests.get(url, params = dictionary)   #Wetter Daten aus der API-Website raus fischen und Anfragen ob alles stimmt (deswegen requests)
        if get_data.status_code == 200:     #200 = Alles Stabilo/OK
            weather_data = get_data.json()
            
            # Übersichtliche Ausgabe der Wetterinformationen
            print("\nWeather Information:")
            print(f"\033[1;35mLocation\033[0m: {weather_data['location']['name']}, {weather_data['location']['country']}")
            print(f"\033[1;35mTemperature\033[0m: {weather_data['current']['temp_c']}°C")
            print(f"\033[1;35mCondition\033[0m: {weather_data['current']['condition']['text']}")
            print(f"\033[1;35mHumidity\033[0m: {weather_data['current']['humidity']}%")
            print(f"\033[1;35mWind Speed\033[0m: {weather_data['current']['wind_kph']} km/h")
            print(f"\033[1;35mLast Updated\033[0m: {weather_data['current']['last_updated']}")
            print()
            print()
            print()
            print("\033[1;33mUsed information above\033[0m: ")
            return weather_data
        else:
            return f"Error while tryning to reach API-Data: {get_data.status_code}!"


    weather_status = get_weather()
    print(weather_status)
    print()
    print()
    choice = input("Please enter the name of the city or the post code: ")
input()

