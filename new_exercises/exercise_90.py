# 教學：綜合練習可以把物件放進清單，再用迴圈、條件與累加器整理資料。
# 每次迴圈檢查目前物件的屬性，符合條件時才呼叫方法或累加數值。
# 範例：
# class Plant:
#     def __init__(self, name, healthy, height):
#         self.name = name
#         self.healthy = healthy
#         self.height = height
#
# plants = [Plant("蘭花", True, 12), Plant("蕨類", False, 8)]
# total_height = 0
# for plant in plants:
#     if plant.healthy:
#         total_height += plant.height
# print(total_height)
# 這會加總健康植物的高度。
#
# 題目 90：整理閱讀紀錄
# 定義 Reading 類別，使用 __init__ 儲存 title、pages 和 completed。
# 新增 show 方法，印出閱讀紀錄的 title 和 pages。
# 建立至少三個 Reading 物件放入 readings 清單，資料需包含已完成和未完成紀錄。
# 用 for 走訪清單，只對 completed 為 True 且 pages 大於或等於 20 的紀錄呼叫 show，
# 同時用累加器計算這些紀錄的總頁數，最後印出總頁數。
