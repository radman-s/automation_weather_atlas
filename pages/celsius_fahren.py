class CelsiusFahrenheit:

    def __init__(self, val):
        self.val = val

    def fahrenheit(self):
        fahre = int(round((9 * self.val) / 5 + 32))
        return f'{fahre}°F'


    def celsius(self):
        cels = int(round((self.val - 32) * 5/9))
        return f'{cels}°C'


