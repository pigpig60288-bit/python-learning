# 教學：可以在同一個 for 迴圈中篩選物件並累加數值。
# 範例：
# class Box:
#     def __init__(self, color, blocks):
#         self.color = color
#         self.blocks = blocks
#
# boxes = [Box("紅", 3), Box("藍", 5)]
# total = 0
# for box in boxes:
#     if box.color == "紅":
#         total += box.blocks
# print(total)
# 只有紅色箱子的 blocks 會被加總。
#
# 題目 70：計算已完成作業的分數
# 定義 Assignment 類別，使用 __init__ 儲存 completed 和 points。
# 建立至少三個 Assignment 物件放入 assignments 清單。
# 用 for 迴圈只累加 completed 為 True 的作業 points，最後印出總分。
