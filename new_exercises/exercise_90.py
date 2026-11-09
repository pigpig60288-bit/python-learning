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
題目 90：整理閱讀紀錄
請依照題意完成程式。

標準輸入範例 1：

records = [ReadingRecord("小明", 30), ReadingRecord("小華", 45)]

預期輸出 1：

小明 30 分鐘\n小華 45 分鐘

標準輸入範例 2：

records = [ReadingRecord("阿雯", 20), ReadingRecord("佩佩", 60)]

預期輸出 2：

阿雯 20 分鐘\n佩佩 60 分鐘
'''