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
題目 62：列出收藏的書名
定義 Book 類別，在 __init__ 中儲存書名 name 和頁數 pages。
新增 show_info 方法，印出「書名 頁數」。
建立 books 清單並用 for 迴圈逐一呼叫每本書的 show_info。

標準輸入範例 1：

books = [Book("小王子", 120), Book("哈利波特", 350)]

預期輸出 1：

小王子 120\n哈利波特 350

標準輸入範例 2：

books = [Book("白雪公主", 90), Book("小鹿斑比", 70)]

預期輸出 2：

白雪公主 90\n小鹿斑比 70
'''