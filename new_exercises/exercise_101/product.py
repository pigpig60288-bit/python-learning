class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        print(f"商品：{self.name}，價格 {self.price}，庫存 {self.stock}")
