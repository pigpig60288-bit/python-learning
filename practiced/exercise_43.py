# 教學：方法可以修改物件自己的屬性。
# 方法透過 self 讀取原本的值，再用賦值更新它。
# 範例：
# class Box:
#     def __init__(self):
#         self.items = 0
#
#     def add_items(self, amount):
#         self.items += amount
#
# box = Box()
# box.add_items(3)
# print(box.items)
# 呼叫 add_items 後，物件保存的 items 數量會增加。
#
# 題目 43：累積跑步里程
# 定義 Runner 類別，__init__ 接收 name，並將 miles 設為 0。
# 新增 add_miles 方法，接收 miles 參數並累加到物件的 miles 屬性。
# 建立一位跑者，呼叫 add_miles(2)，再印出跑者的 miles。
class Runner:
    def __init__(self, name):
        self.name = name
        self.miles = 0

    def add_miles(self, miles):
        self.miles += miles
runner = Runner("小明")
runner.add_miles(2)
print(runner.name, runner.miles)