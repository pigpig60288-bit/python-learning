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
題目 79：避免重複加入收藏景點
請依照題意完成程式。

標準輸入範例 1：

spots = [Spot("日月潭", False), Spot("九份", True)]

預期輸出 1：

日月潭 可加入收藏\n九份 已收藏

標準輸入範例 2：

spots = [Spot("墾丁", True), Spot("阿里山", False)]

預期輸出 2：

墾丁 已收藏\n阿里山 可加入收藏
'''