# Add Celsius class implementation below.
class Celsius:
    def __get__(self, object, value):
        return self._celsius

    def __set__(self, object, value):
        if hasattr(object,'celsius'):
            self._celsius = float(value)
            object.fahrenheit = (value * 9 / 5) + 32

        else:
            self._celsius = (value - 32) * 5 / 9




# Add temperature class implementation below.
class Temperature:
    celsius = Celsius()

    def __init__(self, temp):
        self.fahrenheit = temp
        self.celsius = temp

t1=Temperature(32)
print(t1.fahrenheit)
print(t1.celsius)
t1.celsius=0
print(t1.fahrenheit)
print(t1.celsius)