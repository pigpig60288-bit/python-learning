# 教學：方法可以用參數改變物件數量，再用 if 檢查新的數值。
# 範例：
# class Tank:
#     def __init__(self, water):
#         self.water = water
#
#     def use(self, amount):
#         self.water -= amount
#         if self.water < 3:
#             print("水量偏低")
#
# tank = Tank(8)
# tank.use(6)
# 先更新 water，再依更新後的值判斷。
#
# 題目 86：使用倉庫庫存
# 定義 Stock 類別，使用 __init__ 儲存 name 和 quantity。
# 新增 sell 方法，接收 amount 並從 quantity 扣除。
# 扣除後，若 quantity 小於 5，印出商品名稱和「庫存偏低」。
# 建立一個 Stock 物件，呼叫 sell 並印出剩餘 quantity。
