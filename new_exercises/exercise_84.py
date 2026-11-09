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
題目 84：統計課程完成狀態
請依照題意完成程式。

標準輸入範例 1：

courses = [Course("數學", True), Course("英文", False)]

預期輸出 1：

數學 已完成\n英文 未完成

標準輸入範例 2：

courses = [Course("歷史", True), Course("地理", True)]

預期輸出 2：

歷史 已完成\n地理 已完成
'''