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
題目 55：檢查電池電量
定義 Battery 類別，使用 __init__ 儲存電量 level。
新增 check_level 方法：電量低於 20 時印出「電量偏低」，否則印出「電量足夠」。
建立 Battery 物件並呼叫 check_level。

標準輸入範例 1：

battery = Battery(15)

預期輸出 1：

電量偏低

標準輸入範例 2：

battery = Battery(80)

預期輸出 2：

電量足夠
'''