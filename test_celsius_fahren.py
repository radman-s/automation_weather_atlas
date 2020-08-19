from pages.celsius_fahren import CelsiusFahrenheit
from pages.weather_atlas_page import WeatherAtlasPage
from pages.drivers import Drivers
import time

browser = Drivers('--start-maximized').chrome()

wap = WeatherAtlasPage(driver=browser)

# test start
wap.go()
wap.save_preferences.click()
web_cl_day = wap.temperature_web_day.text()[:-2]
web_cl_nigh = wap.temperature_web_night.text()[:-2]


# switch to fahrenheit
wap.fahrenheit_button.click()

# compare web convert of celsius to fahrenheit day temperature
my_fahre_day = int(CelsiusFahrenheit(int(web_cl_day)).fahrenheit())
web_fahre_day = wap.temperature_web_day.text()[:-2]
assert int(my_fahre_day) == int(web_fahre_day)
print(f'expected day teperature converted to Fahrenheit:   {my_fahre_day}.')
print(f'real day temperature converted to Fahrenheit:      {web_fahre_day}')


# compare web convert of celsius to fahrenheit night temperature
my_fahre_night = int(CelsiusFahrenheit(int(web_cl_nigh)).fahrenheit())
web_fahre_night = wap.temperature_web_night.text()[:-2]
assert int(my_fahre_night) == int(web_fahre_night)
print(f'expected night teperature converted to Fahrenheit: {my_fahre_night}.')
print(f'real night temperature converted to Fahrenheit:    {web_fahre_night}')
print('test passe')

browser.quit()






