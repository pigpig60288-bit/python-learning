# 教學：走訪物件清單時，可用條件挑選數值達標的物件並計數。
# 範例：
# class Visit:
#     def __init__(self, minutes):
#         self.minutes = minutes
#
# visits = [Visit(20), Visit(45), Visit(50)]
# count = 0
# for visit in visits:
#     if visit.minutes >= 40:
#         count += 1
# print(count)
# count 記錄達到時間門檻的參訪次數。
#
# 題目 82：統計金額達標的訂單
# 定義 Order 類別，使用 __init__ 儲存 customer 和 amount。
# 建立至少四個 Order 物件放入 orders 清單。
# 用 for 計算 amount 大於或等於 500 的訂單數量並印出。
