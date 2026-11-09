'''
教學：走訪物件清單時，可以用 if 檢查每個物件的屬性，並只對符合條件的物件呼叫方法。
'''

'''
題目 49：找出庫存不足的商品
定義 Product 類別，使用 __init__ 儲存 name 和 quantity。
新增 show_warning 方法，印出商品名稱和目前庫存數量。
建立至少三個 Product 物件放入 products 清單。
用 for 走訪清單，只對 quantity 小於 5 的商品呼叫 show_warning。

標準輸入範例 1：
products = [
    Product("牙刷", 10),
    Product("牙膏", 4),
    Product("牙線", 3),
]

預期輸出 1：
牙膏 庫存不足，目前剩 4 個
牙線 庫存不足，目前剩 3 個

標準輸入範例 2：
products = [
    Product("杯子", 7),
    Product("毛巾", 2),
    Product("洗面乳", 9),
]

預期輸出 2：
毛巾 庫存不足，目前剩 2 個
'''

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def show_warning(self):
        print(f"{self.name} 庫存不足，目前剩 {self.quantity} 個")


products = [
    Product("牙刷", 10),
    Product("牙膏", 4),
    Product("牙線", 3),
]

for product in products:
    if product.quantity < 5:
        product.show_warning()
