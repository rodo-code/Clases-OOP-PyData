class Product:
    """
    This class is an abstraction for a single product for a store
    """

    def __init__(self, name, brand, price, detail, stock):
        self.name = name
        self.brand = brand
        self.price = price
        self.detail = detail
        self.stock = stock

    def __str__(self):
        return "Product's Name: {}\nBrand: {}\nPrice: {}\nDetail: {}\nStock: {}\n".format(self.name, self.brand,
                                                                                          self.price, self.detail,
                                                                                          self.stock)

    def update_stock(self, new_stock):
        self.stock = new_stock

    def reduce_stock(self):
        self.stock = self.stock - 1

    def update_price(self, new_price):
        self.price = new_price

    def possible_profit(self):
        return self.stock * self.price


# Instance of Products
product1 = Product("Alcohol en Gel", "Eden", 10, "Botella de 200ml", 20)
product2 = Product("Cuadernos", "Top", 2.5, "50 hojas", 100)
product3 = Product("Boligrafos", "Pilot", 3.5, "Color Rojo", 50)
# Printing the products
print(product1)
print(product2)
print(product3)

product1.reduce_stock()
product1.reduce_stock()  # Now the stock of product1 is 18
print(product1)

product2.update_price(3)  # Now the price of product2 is 3
print(product2)

print("The possible profit of product 3 is {}".format(product3.possible_profit()))  # Possible profit of Product 3 is
# 50*3.5=175
