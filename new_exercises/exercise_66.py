# 教學：物件方法可管理自己的清單；len() 可以取得清單項目數量。
# 範例：
# class Drawer:
#     def __init__(self):
#         self.tools = []
#
#     def add_tool(self, tool):
#         self.tools.append(tool)
#
#     def show_count(self):
#         print(len(self.tools))
# 方法能先改變清單，再用 len() 顯示項目數。
#
# 題目 66：管理社團活動
# 定義 Club 類別，使用 __init__ 建立空的 activities 清單。
# 新增 add_activity 方法，接收活動名稱並加入清單。
# 新增 show_count 方法，印出活動數量。
# 建立 Club、加入兩個活動，再呼叫 show_count。
