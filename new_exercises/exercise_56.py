# 教學：方法可比較物件屬性與呼叫時傳入的參數。
# 範例：
# class Container:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def fits(self, amount):
#         if amount <= self.capacity:
#             print("放得下")
#         else:
#             print("放不下")
#
# box = Container(8)
# box.fits(5)
# amount 是每次呼叫時提供的數量，capacity 是物件保存的容量。
#
# 題目 56：檢查座位是否足夠
# 定義 Theater 類別，使用 __init__ 儲存 seats。
# 新增 check_guests 方法，接收 guests 人數。
# 若 guests 小於或等於 seats，印出「座位足夠」，否則印出「座位不足」。
# 建立一個 Theater 物件並呼叫此方法。
