from product import Product

class Customer:
    name = ""
    money = 0
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def buy(self, product: Product, count: int):
        if count <= product.stock:
            if self.money > product.price*count:
                print(f"購買成功：{product.name}")
            else:
                print(f"金額不足，無法購買果汁：總共{product.price*count}元，還需要{product.price*count-self.money}元")
        else:
            print(f"產品數量不足，庫存數量：{product.stock} 購買數量：{count}")