from pages.drivers import Drivers
from pages.weather_atlas_page import WeatherAtlasPage
from pages.current_date import Date


browser = Drivers('--start-maximized').chrome()
wap = WeatherAtlasPage(driver=browser)

# get current date from the module
my_today = Date().time_format()[3:10]

# test start
wap.go()
wap.save_preferences.click()

# get current date from the website
web_today = wap.today_date.text()[-7:]

assert my_today == web_today
print(f'todya: {web_today} is {my_today}')

browser.quit()
print('test passed')
