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
題目 56：檢查座位是否足夠
請依照題意完成程式。

標準輸入範例 1：

classroom = Classroom("A101", 8, 6)

預期輸出 1：

座位足夠：6 個空位

標準輸入範例 2：

classroom = Classroom("B205", 5, 2)

預期輸出 2：

座位不足：2 個空位
'''