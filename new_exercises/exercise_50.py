# 教學：綜合練習可以把多個物件放進清單，再用迴圈和條件判斷處理。
# 每次迴圈取出一個物件後，讀取它的屬性；符合條件時呼叫方法。
# 範例：
# class Ticket:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_name(self):
#         print(self.name)
#
# tickets = [Ticket("小青", 12), Ticket("小明", 20)]
# for ticket in tickets:
#     if ticket.age >= 18:
#         ticket.show_name()
# 這會只顯示年滿 18 歲的乘客姓名。
#
# 題目 50：挑選需要補貨的飲料
# 定義 Drink 類別，使用 __init__ 儲存 name、quantity 和 minimum。
# 新增 show_restock 方法，印出飲料名稱與目前數量。
# 建立至少三個 Drink 物件放入 drinks 清單，設定不同的數量與最低庫存。
# 用 for 走訪清單；當 quantity 小於 minimum 時，呼叫該物件的 show_restock。
