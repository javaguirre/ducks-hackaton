import requests
from lxml import etree

class GWeather():
    ''' Retrieves weather data from google weather API.
        You can put your city.
    '''
    
    def __init__(self, city, country):
        #TODO parse city and country
        self.city = city
        self.country = country
    
    def getData(self):
        data = requests.get("http://www.google.com/ig/api?weather=%s+%s" % (self.city, self.country) )
        doc = etree.fromstring(data.content)
        
        current_conditions = doc.findall("weather/current_conditions")
        forecast_conditions = doc.findall("weather/forecast_conditions")
        
        if current_conditions:
            for child in current_conditions[0].iterchildren():
                print child.get("data")
                
        if forecast_conditions:
            for child in forecast_conditions[0].iterchildren():
                print child.get("data")
