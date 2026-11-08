# 教學：class 可以把相關資料和處理這些資料的方法放在一起。
# 方法可以使用 self 讀取物件屬性，也能用 if/else 依資料做判斷。
# 範例：
# class Plant:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#
#     def show_size(self):
#         if self.height >= 10:
#             print(self.name + "長得很高")
#         else:
#             print(self.name + "還不高")
#
# 這個方法會依植物高度印出不同訊息；題目使用不同情境。
#
# 題目 40：判斷成績是否及格
# 定義 Student 類別，用 __init__ 儲存學生姓名 name 和分數 score。
# 新增 show_result 方法：分數大於或等於 60 時印出「○○及格」，
# 否則印出「○○還要加油」（○換成學生姓名）。
# 建立兩位分數不同的學生物件，分別呼叫 show_result。
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_result(self):
        if self.score >= 60:
            print(f"{self.name}及格")
        else:
            print(f"{self.name}還要加油")
student =Student("阿毛咪", 100)
student.show_result()
student =Student("莊先生", 59)
student.show_result()
