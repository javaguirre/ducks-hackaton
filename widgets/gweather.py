import requests
from lxml import etree

class GWeather():
    ''' Retrieves weather data from google weather API.
        You can put your city.
    '''
    
    def __init__(self, city, country):
        #TODO parse city and country
        self.url = "http://www.google.com/ig/api?weather"
        self.city = city
        self.country = country
    
    def get_data(self):
        current = dict()
        forecast = []
    
        data = requests.get("%s=%s+%s" % (self.url, self.city, self.country) )
        doc = etree.fromstring(data.content)
        
        current_conditions = doc.findall("weather/current_conditions")
        forecast_conditions = doc.findall("weather/forecast_conditions")
        
        if current_conditions:
            for child in current_conditions[0].iterchildren():
                current[child.tag] = child.get("data")
                
        if forecast_conditions:
            for forecast_elem in forecast_conditions:
                aux = dict()
                for child in forecast_elem.iterchildren():
                    aux[child.tag] = child.get("data")
                forecast.append(aux)
        
        return { "current": current, "forecast": forecast }
        
    def convert_to_c(self, temp):
        ''' Converts Fahrenheit to Celsius degrees'''
        return str(round((int(temp) - 32) * (5.0/9.0), 2))
