# 教學：在方法中走訪數字清單時，可以用累加器加總。
# 累加器先設為 0，每次迴圈把目前數字加進去。
# 範例：
# class Pantry:
#     def __init__(self):
#         self.can_counts = [2, 4, 3]
#
#     def total_cans(self):
#         total = 0
#         for count in self.can_counts:
#             total += count
#         print(total)
#
# Pantry().total_cans()
# total 會累積清單中的每個數字。
#
# 題目 58：計算每日步數總和
# 定義 Walker 類別，讓 __init__ 接收 steps 清單並存成屬性。
# 新增 show_total 方法，使用 for 迴圈和累加器計算總步數並印出。
# 建立物件並傳入 [120, 250, 180]，再呼叫 show_total。
