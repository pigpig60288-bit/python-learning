# 教學：可走訪物件清單，用條件挑出物件，再增加符合條件的計數。
# 範例：
# class Candle:
#     def __init__(self, hours):
#         self.hours = hours
#
# candles = [Candle(5), Candle(2), Candle(8)]
# count = 0
# for candle in candles:
#     if candle.hours >= 5:
#         count += 1
# print(count)
# count 是符合 hours 門檻的物件數量。
#
# 題目 80：統計達到目標的閱讀紀錄
# 定義 Reading 類別，使用 __init__ 儲存 title 和 pages。
# 建立至少三個 Reading 物件放入 readings 清單。
# 用 for 計算 pages 大於或等於 20 的紀錄數，最後印出數量。
