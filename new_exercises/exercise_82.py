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
題目 82：統計金額達標的訂單
定義 Order 類別，在 __init__ 中儲存訂單編號 order_id 和金額 amount。
建立 orders 清單，只列出金額至少 400 元的訂單編號。
輸出格式為「金額達標的訂單：訂單編號」。

標準輸入範例 1：

orders = [Order("A001", 450), Order("A002", 280)]

預期輸出 1：

金額達標的訂單：A001

標準輸入範例 2：

orders = [Order("B001", 350), Order("B002", 520)]

預期輸出 2：

金額達標的訂單：B002
'''