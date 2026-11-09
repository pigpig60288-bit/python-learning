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
題目 72：只有營業時才能增加來客數
請依照題意完成程式。

標準輸入範例 1：

customers = [Customer("小青", 20), Customer("小陳", 5)]

預期輸出 1：

小青 來客數：20\n小陳 來客數：5

標準輸入範例 2：

customers = [Customer("小美", 10), Customer("大文", 15)]

預期輸出 2：

小美 來客數：10\n大文 來客數：15
'''