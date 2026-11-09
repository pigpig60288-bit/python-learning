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
題目 75：列出長時間的交通路線
定義 Route 類別，在 __init__ 中儲存路線名稱 name 和行車時間 minutes。
建立 routes 清單，只顯示行車時間至少 20 分鐘的路線，並印出「名稱：時間 分鐘」。
使用 for 迴圈逐一檢查路線。

標準輸入範例 1：

routes = [Route("台北", 35), Route("桃園", 20)]

預期輸出 1：

台北：35 分鐘\n桃園：20 分鐘

標準輸入範例 2：

routes = [Route("高雄", 45), Route("台中", 30)]

預期輸出 2：

高雄：45 分鐘\n台中：30 分鐘
'''