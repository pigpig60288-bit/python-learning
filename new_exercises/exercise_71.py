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
題目 71：顯示餐點資訊
定義 Meal 類別，在 __init__ 中儲存餐點名稱 name 和價格 price。
新增 show_info 方法，印出「餐點名稱：價格 元」。建立 Meal 物件後呼叫此方法。

標準輸入範例 1：

meal = Meal("漢堡", 120)

預期輸出 1：

漢堡：120 元

標準輸入範例 2：

meal = Meal("雞腿飯", 150)

預期輸出 2：

雞腿飯：150 元
'''