# 教學：remove(value) 會從清單中刪除第一個符合 value 的項目。
# 可把 remove 放在物件方法裡，管理該物件的清單。
# 範例：
# class Shelf:
#     def __init__(self):
#         self.labels = ["小說", "雜誌"]
#
#     def remove_label(self, label):
#         if label in self.labels:
#             self.labels.remove(label)
#
# shelf = Shelf()
# shelf.remove_label("小說")
# print(shelf.labels)
# 先用 in 檢查可以避免刪除不存在的項目。
#
# 題目 76：從播放清單移除歌曲
# 定義 Playlist 類別，使用 __init__ 儲存 songs 清單。
# 新增 remove_song 方法，若傳入的歌曲存在就將它移除。
# 建立播放清單，移除其中一首歌曲，再印出更新後的 songs。
