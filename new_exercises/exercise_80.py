'''
教學：符合條件時用計數器加 1，可統計物件清單中達到門檻的筆數。

範例：
class Visitor:
    def __init__(self, minutes):
        self.minutes = minutes

visitors = [Visitor(12), Visitor(25)]
count = 0
for visitor in visitors:
    if visitor.minutes >= 20:
        count += 1

print(f"達標人數：{count}")
'''

'''
題目 80：統計達到目標的閱讀紀錄
定義 ReadingRecord 類別，在 __init__ 中儲存讀者姓名 name 和閱讀分鐘數 minutes。
以 30 分鐘為達標標準，走訪 records 並計算達標紀錄的筆數。
最後印出「達標閱讀紀錄：筆數 筆」；剛好 30 分鐘也算達標。

標準輸入範例 1：

records = [ReadingRecord("小明", 30), ReadingRecord("小華", 45)]

預期輸出 1：

達標閱讀紀錄：2 筆

標準輸入範例 2：

records = [ReadingRecord("阿雯", 20), ReadingRecord("佩佩", 60)]

預期輸出 2：

達標閱讀紀錄：1 筆
'''