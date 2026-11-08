# 教學：可以用多個計數器統計物件清單中不同的狀態。
# 範例：
# class Parcel:
#     def __init__(self, delivered):
#         self.delivered = delivered
#
# parcels = [Parcel(True), Parcel(False), Parcel(True)]
# done = 0
# waiting = 0
# for parcel in parcels:
#     if parcel.delivered:
#         done += 1
#     else:
#         waiting += 1
# print(done, waiting)
# 兩個計數器分別記錄已送達和等待中的包裹。
#
# 題目 78：統計完成與未完成任務
# 定義 Task 類別，使用 __init__ 儲存 is_done。
# 建立至少四個 Task 物件放入 tasks 清單。
# 用 for 迴圈分別計算已完成和未完成的數量，最後印出兩個數量。
