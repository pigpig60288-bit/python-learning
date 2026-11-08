# 教學：方法可以把參數加入物件清單，也可以用 in 檢查清單是否包含資料。
# 範例：
# class Toolbox:
#     def __init__(self):
#         self.names = []
#
#     def add(self, name):
#         self.names.append(name)
#
# toolbox = Toolbox()
# toolbox.add("尺")
# print("尺" in toolbox.names)
# in 的結果可以放在 if 條件中使用。
#
# 題目 73：記錄並檢查參加者
# 定義 Event 類別，建立空的 attendees 清單。
# 新增 register 方法，接收姓名並加入清單。
# 新增 check_attendee 方法，接收姓名並用 in 檢查是否已在清單中，
# 依檢查結果印出不同訊息。加入一位參加者並檢查一次。
