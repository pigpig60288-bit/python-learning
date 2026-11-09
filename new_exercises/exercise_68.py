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
題目 68：找出可參加活動的隊員
定義 Member 類別，在 __init__ 中儲存隊員名稱 name 和是否符合參加資格 eligible。
新增 show_status 方法：eligible 為 True 時印出「名稱 可參加」，否則印出「名稱 不可參加」。
建立 members 清單並逐一呼叫每位隊員的 show_status。

標準輸入範例 1：

members = [Member("小白", True), Member("小明", False)]

預期輸出 1：

小白 可參加\n小明 不可參加

標準輸入範例 2：

members = [Member("阿慶", True), Member("玲玲", True)]

預期輸出 2：

阿慶 可參加\n玲玲 可參加
'''