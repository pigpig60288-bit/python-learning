'''
教學：方法可讀取物件的多個屬性，再用 f-string 把它們組成資訊訊息。

範例：
class Ticket:
    def __init__(self, event, seat):
        self.event = event
        self.seat = seat

    def show_info(self):
        print(f"{self.event}，座位 {self.seat}")

ticket = Ticket("音樂會", "A3")
ticket.show_info()
'''

'''
題目 66：管理社團活動
定義 Activity 類別，在 __init__ 中儲存活動名稱 name 和報名人數 participants。
新增 show_info 方法，印出「活動：名稱，報名人數 人數」。
建立 Activity 物件並呼叫 show_info。

標準輸入範例 1：

activity = Activity("瑜珈", 12)

預期輸出 1：

活動：瑜珈，報名人數 12

標準輸入範例 2：

activity = Activity("烘焙", 8)

預期輸出 2：

活動：烘焙，報名人數 8
'''
class Activity:
    def __init__(self, name, participants):
        self.name = name
        self.participants = participants

    def show_info(self):
        print(f"活動：{self.name}，報名人數 {self.participants}")

activity = Activity("瑜珈", 12)
activity.show_info()