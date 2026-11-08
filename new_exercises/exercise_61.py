# 教學：走訪物件清單時，可檢查每個物件的屬性，只處理符合條件的物件。
# 範例：
# class Package:
#     def __init__(self, label, fragile):
#         self.label = label
#         self.fragile = fragile
#
# packages = [Package("A", True), Package("B", False)]
# for package in packages:
#     if package.fragile:
#         print(package.label)
# 只有 fragile 為 True 的包裹會被列出。
#
# 題目 61：列出需要充電的裝置
# 定義 Device 類別，使用 __init__ 儲存 name 和 battery。
# 新增 show_name 方法，印出裝置名稱。
# 建立至少三個 Device 物件放入 devices 清單，
# 用 for 走訪，只對 battery 小於 20 的裝置呼叫 show_name。
