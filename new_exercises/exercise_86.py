'''
教學：這一題會用到篩選、統計與整理資料的思路。
先把資料存成物件或清單，再用迴圈依序檢查每一筆資料。
如果符合條件，就進行加總、計數、排序或刪除等處理。
這樣寫法可以讓程式更容易閱讀，也更接近實際資料處理的流程。

範例：
items = [
    {"name": "A", "done": True, "points": 5},
    {"name": "B", "done": False, "points": 3},
]

total = 0
for item in items:
    if item["done"]:
        total += item["points"]
print(total)
'''

'''
題目 86：使用倉庫庫存
定義 Warehouse 類別，在 __init__ 中儲存倉庫名稱 name 和庫存 quantity。
新增 use_stock 方法，接收使用數量並更新庫存；範例中每個倉庫都使用 3 個庫存。
新增 show_stock 方法，印出「倉庫名稱 目前剩 數量」。

標準輸入範例 1：

warehouse = Warehouse("A區", 15)
warehouse.use_stock(3)
warehouse.show_stock()

預期輸出 1：

A區 目前剩 12

標準輸入範例 2：

warehouse = Warehouse("B區", 10)
warehouse.use_stock(3)
warehouse.show_stock()

預期輸出 2：

B區 目前剩 7
'''