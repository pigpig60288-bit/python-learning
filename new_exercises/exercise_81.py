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
題目 81：計算商品總價
定義 Item 類別，在 __init__ 中儲存商品名稱 name 和價格 price。
建立 items 清單，使用 for 迴圈累加每項商品的 price，最後印出「總價：金額 元」。

標準輸入範例 1：

items = [Item("筆記本", 30), Item("原子筆", 20)]

預期輸出 1：

總價：50 元

標準輸入範例 2：

items = [Item("資料夾", 45), Item("白板筆", 25)]

預期輸出 2：

總價：70 元
'''