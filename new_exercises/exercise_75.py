# 教學：物件清單中的每個物件都可以有相同名稱的屬性和方法。
# 先用 if 檢查屬性，再呼叫符合條件的物件方法。
# 範例：
# class Course:
#     def __init__(self, title, hours):
#         self.title = title
#         self.hours = hours
#
#     def show(self):
#         print(self.title)
#
# courses = [Course("繪畫", 3), Course("音樂", 1)]
# for course in courses:
#     if course.hours >= 2:
#         course.show()
#
# 題目 75：列出長時間的交通路線
# 定義 Route 類別，儲存 name 和 minutes，並新增 show 方法印出名稱。
# 建立至少三個 Route 物件放入 routes 清單。
# 用 for 走訪，只對 minutes 大於 30 的路線呼叫 show。
