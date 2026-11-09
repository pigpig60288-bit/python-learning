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
請依照題意完成程式。

標準輸入範例 1：
drinks = [Drink("可樂", 3, 5), Drink("水", 8, 5), Drink("茶", 10, 5)]

預期輸出 1：
可樂 目前剩 3，低於最低庫存 5

標準輸入範例 2：
drinks = [Drink("果汁", 6, 5), Drink("牛奶", 2, 4), Drink("咖啡", 9, 5)]

預期輸出 2：
牛奶 目前剩 2，低於最低庫存 4
'''