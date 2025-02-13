class Product:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class Info(Product):


    def info(self):
        return f"{self.name} - {self.price} x {self.quantity}"


class Sell(Product):
    def sell(self, amount):
        if amount > self.quantity:
            print(f"Bizda {self.quantity} ta mahsulot bor xolos")
        else:
            self.quantity -= amount

class Respont(Product):

    def restock(self, amount):
        self.quantity += amount
