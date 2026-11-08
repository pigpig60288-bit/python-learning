# 教學：可在走訪物件時先篩選，再把符合條件物件的數值加進總和。
# 範例：
# class Plant:
#     def __init__(self, ripe, fruits):
#         self.ripe = ripe
#         self.fruits = fruits
#
# plants = [Plant(True, 4), Plant(False, 3), Plant(True, 2)]
# total = 0
# for plant in plants:
#     if plant.ripe:
#         total += plant.fruits
# print(total)
# total 只加總成熟植物的 fruits。
#
# 題目 89：計算通過檢查的包裹總重量
# 定義 Parcel 類別，使用 __init__ 儲存 passed_inspection 和 weight。
# 建立至少三個 Parcel 物件放入 parcels 清單。
# 用 for 只累加 passed_inspection 為 True 的包裹重量，最後印出總重量。
