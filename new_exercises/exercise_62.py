# 教學：方法可以用 for 逐項處理物件屬性中的文字清單。
# 範例：
# class Playlist:
#     def __init__(self):
#         self.titles = ["早晨", "午後"]
#
#     def show_titles(self):
#         for title in self.titles:
#             print(title)
#
# Playlist().show_titles()
# 每次迴圈的 title 都會是清單中的一個文字。
#
# 題目 62：列出收藏的書名
# 定義 Reader 類別，使用 __init__ 接收 titles 清單並存為屬性。
# 新增 show_titles 方法，用 for 迴圈逐項印出所有書名。
# 建立一個 Reader，傳入三個書名並呼叫 show_titles。
