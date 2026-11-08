# 教學：and 可讓篩選條件同時檢查同一物件的兩個屬性。
# 範例：
# class Seat:
#     def __init__(self, near_window, available):
#         self.near_window = near_window
#         self.available = available
#
# seats = [Seat(True, True), Seat(True, False)]
# for seat in seats:
#     if seat.near_window and seat.available:
#         print("符合")
# 兩個條件都成立時才會執行 if 裡的程式。
#
# 題目 85：找出空閒且有設備的教室
# 定義 Room 類別，使用 __init__ 儲存 name、available 和 has_projector。
# 建立至少三個 Room 物件放入 rooms 清單。
# 用 for 只印出 available 和 has_projector 都為 True 的教室名稱。
