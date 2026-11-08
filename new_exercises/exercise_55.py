# 教學：可以用 if/else 檢查物件保存的數值，並印出不同結果。
# 範例：
# class Oven:
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def check(self):
#         if self.temperature >= 180:
#             print("溫度足夠")
#         else:
#             print("還需要加熱")
#
# oven = Oven(200)
# oven.check()
# 判斷使用的是這個物件自己的 temperature。
#
# 題目 55：檢查電池電量
# 定義 Battery 類別，使用 __init__ 儲存 level。
# 新增 check_level 方法：level 小於 20 時印出「電量偏低」，
# 否則印出「電量足夠」。建立一個 Battery 物件並呼叫方法。
