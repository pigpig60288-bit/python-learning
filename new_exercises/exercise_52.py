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
題目 52：記錄電影資料
定義 Movie 類別，並在 __init__ 中儲存電影名稱 name 和上映年份 year。
新增 show_info 方法，印出「電影：名稱（年份）」。建立 Movie 物件後呼叫這個方法。

標準輸入範例 1：

movie = Movie("星際大戰", 2024)

預期輸出 1：

電影：星際大戰（2024）

標準輸入範例 2：

movie = Movie("阿凡達", 2009)

預期輸出 2：

電影：阿凡達（2009）
'''