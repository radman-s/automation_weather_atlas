class CelsiusFahrenheit:

    def __init__(self, val):
        self.val = val

    def fahrenheit(self):
        fahre = round((9 * self.val) / 5 + 32)
        return fahre


    def celsius(self):
        cels = round((self.val - 32) * 5/9)
        return cels


