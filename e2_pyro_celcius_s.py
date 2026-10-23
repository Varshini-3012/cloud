
import Pyro4

@Pyro4.expose
class Temperature:
    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9

daemon = Pyro4.Daemon()
uri = daemon.register(Temperature())

print("Temperature RMI Server is running...")
print("URI:", uri)

daemon.requestLoop()
