# 教學：在 for 迴圈中搭配 if，可以計算清單內符合條件的項目數。
# 每遇到一個符合條件的項目，就增加計數器。
# 範例：
# class Workshop:
#     def __init__(self):
#         self.durations = [15, 40, 25]
#
#     def count_long(self):
#         count = 0
#         for duration in self.durations:
#             if duration >= 30:
#                 count += 1
#         print(count)
#
# Workshop().count_long()
# count 記錄符合時間門檻的活動數量。
#
# 題目 59：計算高於標準的溫度筆數
# 定義 Weather 類別，使用 __init__ 儲存 temperatures 清單。
# 新增 count_warm 方法，計算大於 25 的溫度有幾筆並印出。
# 建立物件並傳入 [18, 27, 25, 30, 22]，再呼叫 count_warm。
