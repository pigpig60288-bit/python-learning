'''
教學：物件可把名稱和數量存成屬性，方法用 if/else 依數量回報狀態。

範例：
class Box:
    def __init__(self, label, count):
        self.label = label
        self.count = count

    def show_status(self):
        if self.count > 0:
            print(f"{self.label} 有內容物")
        else:
            print(f"{self.label} 是空的")

box = Box("藍盒", 2)
box.show_status()
'''

'''
題目 65：統計有庫存的商品
定義 Product 類別，在 __init__ 中儲存商品名稱 name 和庫存數量 quantity。
新增 show_status 方法：庫存大於 0 時印出「名稱 有庫存」，否則印出「名稱 尚未補貨」。
建立 products 清單並逐一呼叫每個商品的 show_status。

標準輸入範例 1：

products = [Product("鉛筆", 4), Product("橡皮擦", 6)]

預期輸出 1：

鉛筆 有庫存\n橡皮擦 有庫存

標準輸入範例 2：

products = [Product("筆記本", 3), Product("色筆", 7)]

預期輸出 2：

筆記本 有庫存\n色筆 有庫存
'''