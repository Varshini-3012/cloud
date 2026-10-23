
import Pyro4

uri = input("Enter server URI: ")
shopping = Pyro4.Proxy(uri)

print("\nAvailable Products:")
print("Laptop - Rs. 50000")
print("Phone - Rs. 20000")
print("Headphones - Rs. 2000")

product = input("Enter product name: ").title()
quantity = int(input("Enter quantity: "))

bill = shopping.calculate_bill(product, quantity)

if "error" in bill:
    print(bill["error"])
else:
    print("\nShopping Bill")
    print("Product:", bill["product"])
    print("Quantity:", bill["quantity"])
    print("Total: Rs.", bill["total"])
    print("Discount: Rs.", bill["discount"])
    print("Final Amount: Rs.", bill["final_amount"])

shopping._pyroRelease()
