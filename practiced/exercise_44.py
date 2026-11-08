# 教學：方法可以使用 if/else，依物件屬性的值做不同處理。
# 範例：
# class Battery:
#     def __init__(self, charge):
#         self.charge = charge
#
#     def check(self):
#         if self.charge > 0:
#             print("還有電")
#         else:
#             print("需要充電")
#
# Battery(5).check()
# check 會根據這個物件的 charge 值選擇訊息。
#
# 題目 44：檢查植物是否需要澆水
# 定義 Plant 類別，使用 __init__ 儲存 name 和 water_level。
# 新增 check_water 方法：water_level 小於 3 時印出植物名稱和「需要澆水」，
# 否則印出植物名稱和「目前水分足夠」。
# 建立一株 water_level 為 2 的植物，呼叫 check_water。
class Plant:
    def __init__(self, name, water_level):
        self.name = name
        self.water_level = water_level
    def check_water(self):
        if self.water_level < 3:
            print(f"{self.name}需要澆水")
        else:
            print(f"{self.name}目前水分足夠")
plant = Plant("菠菜", 2)
plant.check_water()