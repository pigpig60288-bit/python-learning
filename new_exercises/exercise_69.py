# 教學：篩選物件後，可以呼叫它的方法修改自己的資料。
# 範例：
# class Score:
#     def __init__(self, points):
#         self.points = points
#
#     def add_bonus(self):
#         self.points += 2
#
# scores = [Score(5), Score(9)]
# for score in scores:
#     if score.points < 7:
#         score.add_bonus()
# 條件成立的物件才會增加 points。
#
# 題目 69：替低電量裝置充電
# 定義 Device 類別，使用 __init__ 儲存 name 和 battery。
# 新增 charge 方法，將 battery 增加 10。
# 建立至少三個 Device 物件放入 devices 清單；
# 用 for 走訪，只對 battery 小於 30 的裝置呼叫 charge。
# 最後逐一印出所有裝置的 name 和 battery。
