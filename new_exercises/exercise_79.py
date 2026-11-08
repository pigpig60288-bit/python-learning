# 教學：方法可以檢查清單中是否有參數指定的項目，再修改清單。
# 範例：
# class Box:
#     def __init__(self):
#         self.colors = ["綠", "黃"]
#
#     def add_color(self, color):
#         if color not in self.colors:
#             self.colors.append(color)
#
# 這樣相同的顏色不會被重複加入。
#
# 題目 79：避免重複加入收藏景點
# 定義 Traveler 類別，建立空的 places 清單。
# 新增 save_place 方法：只有傳入的地點不在 places 中時才加入。
# 建立物件，對同一地點呼叫兩次，再印出 places 確認沒有重複項目。
