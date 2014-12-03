import urllib
import json

url = "http://api.openweathermap.org/data/2.5/weather?q=Birmingham,uk"

response = urllib.urlopen(url).read()
data = json.loads(response.decode('utf8'))
temp = float(data['main']['temp']) - 273.15
print temp
