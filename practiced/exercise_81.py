'''
教學：把數字屬性逐一加入累加器，就能算出物件清單中的總和。

範例：
class Package:
    def __init__(self, weight):
        self.weight = weight

packages = [Package(2), Package(4)]
total_weight = 0
for package in packages:
    total_weight += package.weight

print(total_weight)
'''

'''
題目 81：計算商品總價
定義 Item 類別，在 __init__ 中儲存商品名稱 name 和價格 price。
建立 items 清單，使用 for 迴圈累加每項商品的 price，最後印出「總價：金額 元」。

標準輸入範例 1：

items = [Item("筆記本", 30), Item("原子筆", 20)]

預期輸出 1：

總價：50 元

標準輸入範例 2：

items = [Item("資料夾", 45), Item("白板筆", 25)]

預期輸出 2：

總價：70 元
'''
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

total = 0
items = [Item("筆記本", 30), Item("原子筆", 20)]

for item in items:
    total += item.price
print(f"總價：{total} 元") 