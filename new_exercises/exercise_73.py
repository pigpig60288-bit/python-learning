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
題目 73：記錄並檢查參加者
定義 Participant 類別，在 __init__ 中儲存參加者姓名 name 和是否已參加 attended。
新增 show_status 方法：attended 為 True 時印出「姓名 已參加」，否則印出「姓名 未參加」。
建立 participants 清單並逐一呼叫每個物件的 show_status。

標準輸入範例 1：

participants = [Participant("小榮", True), Participant("小文", False)]

預期輸出 1：

小榮 已參加\n小文 未參加

標準輸入範例 2：

participants = [Participant("阿傑", True), Participant("依依", True)]

預期輸出 2：

阿傑 已參加\n依依 已參加
'''