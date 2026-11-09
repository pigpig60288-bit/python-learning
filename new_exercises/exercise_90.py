'''
教學：方法可讀取物件屬性並格式化輸出；物件清單可用 for 逐一呼叫方法。

範例：
class Ticket:
    def __init__(self, event, seat):
        self.event = event
        self.seat = seat

    def show_info(self):
        print(f"{self.event}，座位 {self.seat}")

tickets = [Ticket("音樂會", "A3"), Ticket("舞台劇", "B2")]
for ticket in tickets:
    ticket.show_info()
'''

'''
題目 90：整理閱讀紀錄
定義 ReadingRecord 類別，在 __init__ 中儲存讀者姓名 name 和閱讀分鐘數 minutes。
新增 show_info 方法，印出「姓名 分鐘數 分鐘」。
建立 records 清單並用 for 迴圈逐一呼叫每筆紀錄的 show_info。

標準輸入範例 1：

records = [ReadingRecord("小明", 30), ReadingRecord("小華", 45)]

預期輸出 1：

小明 30 分鐘\n小華 45 分鐘

標準輸入範例 2：

records = [ReadingRecord("阿雯", 20), ReadingRecord("佩佩", 60)]

預期輸出 2：

阿雯 20 分鐘\n佩佩 60 分鐘
'''