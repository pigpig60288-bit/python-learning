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
題目 70：計算已完成作業的分數
請依照題意完成程式。

標準輸入範例 1：

homework = [Grade("小華", 88), Grade("小美", 70)]

預期輸出 1：

小華 已完成\n小美 未完成

標準輸入範例 2：

homework = [Grade("阿強", 95), Grade("志明", 60)]

預期輸出 2：

阿強 已完成\n志明 已完成
'''