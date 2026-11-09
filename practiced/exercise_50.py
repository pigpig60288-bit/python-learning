'''
教學：這一題會用到物件、清單與條件判斷。
先把資料放進物件裡，再把物件存進清單，最後用 for 迴圈逐一取出。
當你拿到某個物件時，可以用 if 檢查它的屬性，確認它是否符合條件。
只有符合條件的物件才該被修改、計算或印出結果。

範例：
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

items = [Product("杯子", 3), Product("筆記本", 7)]
for item in items:
    if item.stock < 5:
        print(item.name)
'''

'''
題目 50：挑選需要補貨的飲料
請完成以下內容：
1. 定義 Drink 類別，並在 __init__ 中儲存飲料名稱 name、目前庫存 stock，以及最低庫存 min。
2. 新增 show_warning 方法。當目前庫存 stock 小於這個飲料自己的最低庫存 min 時，印出飲料名稱、目前庫存和最低庫存；否則不印出訊息。
3. 建立 drinks 清單，並用 for 迴圈走訪清單，對每個飲料呼叫 show_warning。

注意：每種飲料的最低庫存可能不同，判斷時要使用該物件的 min，不要把最低庫存固定寫成同一個數字。

標準輸入範例 1：
drinks = [Drink("可樂", 3, 5), Drink("水", 8, 5), Drink("茶", 10, 5)]

預期輸出 1：
可樂 目前剩 3，低於最低庫存 5

標準輸入範例 2：
drinks = [Drink("果汁", 6, 5), Drink("牛奶", 2, 4), Drink("咖啡", 9, 5)]

預期輸出 2：
牛奶 目前剩 2，低於最低庫存 4
'''


class Drink:
    def __init__(self, name, stock, min):
        self.name = name
        self.stock = stock
        self.min = min
    def show_warning(self):
        if self.stock < self.min:
            print(f"{self.name}目前剩{self.stock}，低於最低庫存{self.min}")

drinks = [Drink("可樂", 3, 5), Drink("水", 8, 5), Drink("茶", 10, 5)]

'''
for i in range(len(drinks)):
    drink = drinks[i]
    if drink.stock < drink.min:
        print(f"{drink.name}目前剩{drink.stock}，低於最低庫存{drink.min}")
'''

for drink in drinks:
    drink.show_warning()