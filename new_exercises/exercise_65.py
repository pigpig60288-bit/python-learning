'''
教學：這一題會練習把資料整理成物件，然後用條件控制處理邏輯。
每個物件可以存很多資訊，例如 name、score、stock、status 等屬性。
用 for 迴圈走訪清單時，可以依序取出每個物件，再用 if 判斷它是否符合條件。
如果符合條件，就更新資料、計算結果，或印出需要注意的內容。

範例：
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("小明", 90), Student("小華", 60)]
for student in students:
    if student.score >= 80:
        print(student.name)
'''

'''
題目 65：統計有庫存的商品
定義 Product 類別，在 __init__ 中儲存商品名稱 name 和庫存數量 quantity。
新增 show_status 方法：庫存大於 0 時印出「名稱 有庫存」，否則印出「名稱 尚未補貨」。
建立 products 清單並逐一呼叫每個商品的 show_status。

標準輸入範例 1：

products = [Product("鉛筆", 4), Product("橡皮擦", 6)]

預期輸出 1：

鉛筆 尚未補貨\n橡皮擦 有庫存

標準輸入範例 2：

products = [Product("筆記本", 3), Product("色筆", 7)]

預期輸出 2：

筆記本 尚未補貨\n色筆 有庫存
'''