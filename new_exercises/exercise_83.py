# 教學：可用方法把新項目加入物件清單，並用 in 檢查某項資料是否存在。
# 範例：
# class Board:
#     def __init__(self):
#         self.notes = []
#
#     def add_note(self, note):
#         self.notes.append(note)
#
# board = Board()
# board.add_note("打電話")
# print("打電話" in board.notes)
# in 會檢查指定文字是否出現在清單裡。
#
# 題目 83：管理每日任務
# 定義 Planner 類別，建立空的 tasks 清單。
# 新增 add_task 方法加入任務，新增 has_task 方法用 in 檢查任務。
# 加入兩項任務，並檢查其中一項存在的任務。
