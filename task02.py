from weather import Weather
weather = Weather()


area= weather.lookup_by_location("halifax")
cond=area.condition()
forecast=area.forecast()
print(forecast)
