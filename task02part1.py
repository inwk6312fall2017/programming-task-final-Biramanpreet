from weather import Weather
weather = Weather

location = weather.lookup_by_location('Halifax')
condition = location.condition('Halifax')
print (condition['text'])
forecast = location.forecast()
hightemp=[]
lowtemp=[]
print("current weather is ", condition['text'])
print("current temperature ",condition['temp'])
print("next 5 days")
for forecasts in location.forecast():
        hightemp = forecasts['high']
        lowtemp = forecasts['low']
        rain= forecast['text']
        if forecasts['text']== "Rain":
                print("It will rain on",forecasts['day'])
