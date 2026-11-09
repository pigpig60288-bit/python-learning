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
題目 59：計算高於標準的溫度筆數
使用 for 迴圈走訪 temperatures 清單，計算高於 23 度的溫度有幾筆。
最後印出「高於標準的溫度：筆數 筆」；等於 23 度不算高於標準。

標準輸入範例 1：

temperatures = [18, 25, 30]

預期輸出 1：

高於標準的溫度：2 筆

標準輸入範例 2：

temperatures = [20, 21, 24]

預期輸出 2：

高於標準的溫度：1 筆
'''