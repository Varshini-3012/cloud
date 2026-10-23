
import Pyro4

uri = input("Enter server URI: ")
temperature = Pyro4.Proxy(uri)

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter choice: ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", temperature.celsius_to_fahrenheit(c))

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", temperature.fahrenheit_to_celsius(f))

else:
    print("Invalid choice")

temperature._pyroRelease()
