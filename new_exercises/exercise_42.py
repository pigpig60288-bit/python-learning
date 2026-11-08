# 教學：一個物件可以有多個屬性，分別保存不同資料。
# 在 __init__ 裡用 self.屬性名稱儲存傳入的資料。
# 範例：
# class Room:
#     def __init__(self, floor, number):
#         self.floor = floor
#         self.number = number
#
# room = Room(2, 8)
# print(room.floor)
# room.floor 和 room.number 是這個房間物件各自保存的資料。
#
# 題目 42：記錄書籍資料
# 定義 Book 類別，使用 __init__ 接收 title 和 author，
# 並分別存成物件屬性。
# 建立一本書，書名為「雲朵旅行」，作者為「小林」，
# 分別印出這本書的 title 和 author。
