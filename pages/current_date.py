import datetime

class Date:

    def get_time(self):
        date_time = str(datetime.datetime.now())
        return date_time[:10]

    def time_format(self):
        date_time = datetime.datetime.strptime(self.get_time(), '%Y-%m-%d')
        return datetime.date.strftime(date_time, '%y %d. %B')