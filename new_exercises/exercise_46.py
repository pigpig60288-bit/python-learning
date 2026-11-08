# 教學：清單可以存成物件屬性，讓每個物件保有自己的清單。
# 用 self.items = [] 建立清單，再透過 append() 加入新項目。
# 範例：
# class Bag:
#     def __init__(self):
#         self.snacks = []
#
#     def add_snack(self, snack):
#         self.snacks.append(snack)
#
# bag = Bag()
# bag.add_snack("餅乾")
# print(bag.snacks)
# 呼叫 add_snack 會把一項資料加入這個 Bag 物件的清單。
#
# 題目 46：記錄寵物玩具
# 定義 Pet 類別，使用 __init__ 儲存 name，並建立空的 toys 清單。
# 新增 add_toy 方法，接收 toy 參數並加到 toys 清單。
# 建立一隻寵物，呼叫 add_toy 加入「球」，再印出它的 toys 清單。
