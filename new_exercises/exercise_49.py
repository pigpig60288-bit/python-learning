# 教學：走訪物件清單時，可以用 if 檢查每個物件的屬性，
# 只對符合條件的物件執行方法。
# 範例：
# class Toy:
#     def __init__(self, name, is_new):
#         self.name = name
#         self.is_new = is_new
#
# toys = [Toy("風箏", True), Toy("積木", False)]
# for toy in toys:
#     if toy.is_new:
#         print(toy.name)
# 只有 is_new 為 True 的物件名稱會被印出。
#
# 題目 49：找出庫存不足的商品
# 定義 Product 類別，使用 __init__ 儲存 name 和 quantity。
# 新增 show_warning 方法，印出商品名稱和目前庫存數量。
# 建立至少三個 Product 物件放入 products 清單。
# 用 for 走訪清單，只對 quantity 小於 5 的商品呼叫 show_warning。
