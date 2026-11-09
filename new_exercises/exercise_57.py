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
題目 57：收集旅行城市
請依照題意完成程式。

標準輸入範例 1：

cities = ["台北", "東京", "大阪"]

預期輸出 1：

台北\n東京\n大阪

標準輸入範例 2：

cities = ["首爾", "札幌", "香港"]

預期輸出 2：

首爾\n札幌\n香港
'''