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
題目 54：記錄游泳距離
定義 Swimmer 類別，在 __init__ 中儲存名字 name，並將游泳距離 distance 設為 0。
新增 add_distance 方法，接收距離並累加到 distance；再新增 show_distance 方法印出目前總距離。
建立 Swimmer 物件後，依範例呼叫 add_distance，再呼叫 show_distance。

標準輸入範例 1：

swimmer = Swimmer("小安")
swimmer.add_distance(8)
swimmer.show_distance()

預期輸出 1：

游泳距離：8

標準輸入範例 2：

swimmer = Swimmer("阿傑")
swimmer.add_distance(6)
swimmer.show_distance()

預期輸出 2：

游泳距離：6
'''