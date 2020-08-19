from pages.celsius_fahren import CelsiusFahrenheit
from pages.weather_atlas_page import WeatherAtlasPage
from pages.drivers import Drivers
import time

browser = Drivers('--start_maximized').chrome()

wap = WeatherAtlasPage(driver=browser)

# test start
wap.go()
wap.save_preferences.click()
web_cl_day = wap.temperature_web_day.text()
web_cl_nigh = wap.temperature_web_night.text()



print(web_cl_day)
print(web_cl_nigh)

wap.fahrenheit_button.click()

my_fahre_day = int(CelsiusFahrenheit(web_cl_day).fahrenheit())
print(f'my: {my_fahre_day}')
my_fahre_night = int(CelsiusFahrenheit(web_cl_nigh).fahrenheit())
print(f'my: {my_fahre_night}')



web_fahr_day = wap.temperature_web_day.text()
web_fahr_night = wap.temperature_web_night.text()

print(web_fahr_day)
print(web_fahr_night)










