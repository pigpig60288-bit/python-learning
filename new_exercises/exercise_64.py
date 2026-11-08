# 教學：方法可以依物件狀態判斷是否接受傳入的資料。
# 範例：
# class Locker:
#     def __init__(self, is_open):
#         self.is_open = is_open
#
#     def store(self, item):
#         if self.is_open:
#             print("已放入" + item)
#         else:
#             print("置物櫃未開")
#
# Locker(True).store("外套")
# 方法同時使用 is_open 屬性和 item 參數。
#
# 題目 64：確認會員能否借書
# 定義 Member 類別，使用 __init__ 儲存 name 和 active。
# 新增 borrow 方法，接收 book_name。
# active 為 True 時印出會員姓名與借閱書名，否則印出「會員資格未啟用」。
# 建立一位會員並呼叫 borrow。
