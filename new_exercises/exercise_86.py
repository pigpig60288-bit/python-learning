'''
教學：方法參數可以代表要扣除的數量，再用 -= 更新物件原有的屬性。

範例：
class Jar:
    def __init__(self, candies):
        self.candies = candies

    def eat(self, amount):
        self.candies -= amount

jar = Jar(10)
jar.eat(3)
print(jar.candies)
'''

'''
題目 86：使用倉庫庫存
定義 Warehouse 類別，在 __init__ 中儲存倉庫名稱 name 和庫存 quantity。
新增 use_stock 方法，接收使用數量並更新庫存；範例中每個倉庫都使用 3 個庫存。
新增 show_stock 方法，印出「倉庫名稱 目前剩 數量」。

標準輸入範例 1：

warehouse = Warehouse("A區", 15)
warehouse.use_stock(3)
warehouse.show_stock()

預期輸出 1：

A區 目前剩 12

標準輸入範例 2：

warehouse = Warehouse("B區", 10)
warehouse.use_stock(3)
warehouse.show_stock()

預期輸出 2：

B區 目前剩 7
'''