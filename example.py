#!/usr/bin/python

from ducksapi import DuckClientApi
from widgets.blue_presence import BluePresence
from widgets.machine import MachineStat
from widgets.gweather import GWeather
from widgets.github import Github
import time

def main():
    #TODO check values
    #TODO check datetime of last requests
    apikey = raw_input("Please enter your API Key: ")
    endpoint = raw_input("Please enter your first endpoint: ")

    d = DuckClientApi(apikey, endpoint)
    
    #Bluetooth presence
    b = BluePresence()
    #b.set_user("example", 'xx:xx:xx:xx:xx:xx', "Fullname") #macs of users registered
    #b.set_user("example2", 'xx:xx:xx:xx:xx:xx', "Fullname")
    
    #TODO Do it as a cron job, or use somthing like Kronos API
    while True:

######## Bluetooth #############
        users = b.get_users_list()
        if users:
            d.endpoint = "12324"
            d.update_tl("Bluetooth - Now at the office", users)
        
######## Machine Stats ###########
        m = MachineStat()
        d.endpoint = "11780"
        d.update_count(m.get_cpu())
        d.endpoint = "11782"
        d.update_count(m.get_ram())
        d.endpoint = "11783"
        
######## Google weather ##########
        city = "madrid"
        country = "spain"
        g = GWeather(city, country)
        weather = g.get_data()
        d.endpoint = "12317" # Temperature in Celsius
        d.update_count(weather['current']['temp_c'])
        d.endpoint = "12319" # Humidity percent
        d.update_count(weather['current']['humidity'][-3:-1])
        d.endpoint = "12318" # Highest temperature in Fahrenheit
        d.update_count(weather['current']['temp_f'])
        
        d.endpoint = "12326"
        d.update_small_image("http://www.google.com%s" % weather['current']['icon'], "%s(%s) - %s" % ( city, country, weather['current']['condition']))
        
        d.endpoint = "11785"
        for el in weather['forecast']:
            d.update_tl(el['condition'], "Day: %s , High Temp: %s, Low Temp: %s" % (
                    el['day_of_week'], g.convert_to_c(el['high']), g.convert_to_c(el['low'])), "http://www.google.com%s" % el['icon']
                    )
            time.sleep(2)
        
        
        
########GITHUB #########
        g = Github("django", "django", "master")
        commits = g.get_commits()
        d.endpoint = "12323"
        #TODO format date
        for commit in commits['commits'][0:5]: #last five commits
            d.update_tl("%s: %s - %s" % (g.repo, commit['committer']['name'], commit['committed_date']), commit['message'])
            time.sleep(2)
        
        #g.user = "django"
        #g.repo = "django"
        #g.get_issues( "open", "master")
        
        #We wait for 5 minutes
        time.sleep(5*60)
    
    
if __name__ == '__main__':
    main()
