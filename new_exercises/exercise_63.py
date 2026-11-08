# 教學：更新物件屬性後，可以再讀取它來確認新的狀態。
# 範例：
# class Meter:
#     def __init__(self, value):
#         self.value = value
#
#     def increase(self, amount):
#         self.value += amount
#
# meter = Meter(10)
# meter.increase(5)
# print(meter.value)
# increase 改變物件保存的 value。
#
# 題目 63：增加花盆中的花朵數
# 定義 FlowerPot 類別，__init__ 接收 flowers 數量。
# 新增 plant 方法，接收 amount 並將它加到 flowers。
# 建立一個花盆，呼叫 plant 增加 2 朵花，再印出 flowers。
