
import Pyro4

@Pyro4.expose
class Shopping:
    products = {
        "Laptop": 50000,
        "Phone": 20000,
        "Headphones": 2000
    }

    def calculate_bill(self, product_name, quantity):
        if product_name not in self.products:
            return {"error": "Product not found"}

        if quantity <= 0:
            return {"error": "Quantity must be greater than zero"}

        price = self.products[product_name]
        total = price * quantity

        if total >= 50000:
            discount = total * 0.10
        else:
            discount = total * 0.05

        final_amount = total - discount

        return {
            "product": product_name,
            "quantity": quantity,
            "total": total,
            "discount": discount,
            "final_amount": final_amount
        }

daemon = Pyro4.Daemon()
uri = daemon.register(Shopping())

print("Shopping RMI Server is running...")
print("URI:", uri)

daemon.requestLoop()
