# 教學：可以在走訪物件清單時，以累加器統計符合條件的物件數量。
# 範例：
# class Lamp:
#     def __init__(self, working):
#         self.working = working
#
# lamps = [Lamp(True), Lamp(False), Lamp(True)]
# count = 0
# for lamp in lamps:
#     if lamp.working:
#         count += 1
# print(count)
# count 最後會是正常運作的燈具數量。
#
# 題目 65：統計有庫存的商品
# 定義 Product 類別，使用 __init__ 儲存 quantity。
# 建立至少三個 Product 物件放入 products 清單。
# 用 for 迴圈計算 quantity 大於 0 的商品數量並印出。
