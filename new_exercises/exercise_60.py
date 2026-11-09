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
題目 60：讓多台機器回報狀態
定義 Machine 類別，在 __init__ 中儲存機器名稱 name 和狀態 status。
新增 show_status 方法，印出「名稱 狀態」。
建立 machines 清單並用 for 迴圈逐一呼叫每台機器的 show_status。

標準輸入範例 1：

machines = [Machine("A", "正常"), Machine("B", "故障")]

預期輸出 1：

A 正常\nB 故障

標準輸入範例 2：

machines = [Machine("C", "正常"), Machine("D", "故障")]

預期輸出 2：

C 正常\nD 故障
'''