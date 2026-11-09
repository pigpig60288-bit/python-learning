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
題目 64：確認會員能否借書
定義 Member 類別，在 __init__ 中儲存會員名稱 name 和目前借閱本數 borrowed_count。
新增 check_borrow 方法：借閱本數大於 0 時印出「名稱 可以借書」，否則印出「名稱 不能借書」。
建立 Member 物件並呼叫 check_borrow。

標準輸入範例 1：

member = Member("小明", 2)

預期輸出 1：

小明 可以借書

標準輸入範例 2：

member = Member("阿美", 0)

預期輸出 2：

阿美 不能借書
'''