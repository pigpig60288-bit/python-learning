# 教學：方法可以先檢查物件狀態，只有狀態符合時才修改屬性。
# 範例：
# class Gate:
#     def __init__(self, open):
#         self.open = open
#         self.visitors = 0
#
#     def enter(self):
#         if self.open:
#             self.visitors += 1
#
# gate = Gate(True)
# gate.enter()
# print(gate.visitors)
# 門關閉時，enter 不會增加 visitors。
#
# 題目 72：只有營業時才能增加來客數
# 定義 Shop 類別，使用 __init__ 儲存 is_open，並將 visitors 設為 0。
# 新增 welcome 方法：is_open 為 True 時將 visitors 加 1；
# 否則保持原值。建立一間營業中的店，呼叫 welcome，再印出 visitors。
