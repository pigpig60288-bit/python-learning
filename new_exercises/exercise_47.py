# 教學：方法可以用 for 逐項走訪物件屬性中的清單。
# 若要計算符合條件的項目數量，可以先將計數變數設為 0，
# 每找到一項符合條件的資料，就把計數加 1。
# 範例：
# class Garden:
#     def __init__(self):
#         self.heights = [4, 12, 7]
#
#     def count_tall(self):
#         total = 0
#         for height in self.heights:
#             if height >= 10:
#                 total += 1
#         print(total)
# 這個方法會印出高度至少 10 的植物數量。
#
# 題目 47：計算及格人數
# 定義 ClassRoom 類別，使用 __init__ 將 scores 清單存成物件屬性。
# 新增 count_passed 方法，計算分數大於或等於 60 的項目數量並印出。
# 建立一個物件，傳入分數清單 [72, 45, 88, 59]，呼叫 count_passed。
