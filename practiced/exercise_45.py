'''
教學：方法的參數可以和物件屬性一起用在條件判斷中。
範例：
class Wallet:
def __init__(self, money):
self.money = money
def can_buy(self, cost):
if self.money >= cost:
print("買得起")
else:
print("還不夠")
Wallet(100).can_buy(30)
cost 是呼叫方法時傳入的資料，money 則是物件保存的資料。
'''

'''
題目 45：檢查是否達成閱讀目標
定義 Reader 類別，使用 __init__ 儲存 name 和 pages_read。
新增 check_goal 方法，接收 goal 頁數：
pages_read 大於或等於 goal 時，印出讀者名稱和「已達標」，
否則印出讀者名稱和「尚未達標」。
建立一位已讀 25 頁的讀者，呼叫 check_goal 並傳入一個目標頁數。
'''

class Reader:
    def __init__(self, name, pages_read):
        self.name = name
        self.pages_read = pages_read
    def check_goal(self, goal):
        if self.pages_read >= goal:
            print(f"{self.name}已達標")
        else:
            print(f"{self.name}尚未達標")
reader = Reader("林昀昀", 25)
reader.check_goal(20)
