from weather import Weather
weather = Weather()

area=weather.lookup_by_location('halifax')
cond=area.condition()
days=[]
x=0
for forecasts in area.forecast():
    if x<5:
        newlist=[]
        newlist.append(forecasts['text'])
        newlist.append(forecasts['date'])
        newlist.append(forecasts['high'])
        newlist.append(forecasts['low'])
        days.append(newlist)
        x=x+1
print (days)
