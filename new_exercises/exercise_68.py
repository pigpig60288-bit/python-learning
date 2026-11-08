# 教學：and 可以要求兩個條件同時成立，才處理該物件。
# 範例：
# class Plant:
#     def __init__(self, sunny, watered):
#         self.sunny = sunny
#         self.watered = watered
#
# plants = [Plant(True, True), Plant(True, False)]
# for plant in plants:
#     if plant.sunny and plant.watered:
#         print("狀態良好")
# 只有兩個屬性都符合條件時才會印出訊息。
#
# 題目 68：找出可參加活動的隊員
# 定義 Player 類別，使用 __init__ 儲存 name、registered 和 paid。
# 建立至少三個 Player 物件放入 players 清單。
# 用 for 走訪，只在 registered 和 paid 都為 True 時印出隊員姓名。
