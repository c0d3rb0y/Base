if __name__ == "__main__":
    print("This is a BaseAI module, not a standalone script. Please put this in the comp_mods folder inside of the base folder to use this command.")
else:
    from base.utils import *
    try:
        import python_weather
    except:
        print("python_weather not found! attempting install...")
        os.system('cmd /c "pip install python-weather"')
        import python_weather
    try:
        import asyncio
    except:
        print("asyncio not found! attempting install...")
        os.system('cmd /c "pip install asyncio"')
        import asyncio

    speak("What city?")
    city = input("City name: ")
    speak("What state?")
    state = input("State (2 letters): ")
    if(len(state) > 2):
        speak("Try again.")
        print("For example, Hawaii is HI and Oklahoma is OK.")
        state = input("State (2 letters): ")

    async def getweather(c, s):
        # declare the client. format defaults to metric system (celcius, km/h, etc.)
        client = python_weather.Client(format=python_weather.IMPERIAL)

        # fetch a weather forecast from a city
        weather = await client.find(c + " " + s)

        # returns the current day's forecast temperature (int)
        speak("It is currently " + str(weather.current.temperature) + " degrees fahrenheit.")
        print("Currently " + str(weather.current.temperature) + "F")

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            print(str(forecast.date), forecast.sky_text, forecast.temperature)

        # close the wrapper once done
        await client.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather(city, state))