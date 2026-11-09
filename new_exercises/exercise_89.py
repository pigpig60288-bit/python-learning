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
題目 89：計算通過檢查的包裹總重量
定義 Parcel 類別，在 __init__ 中儲存包裹編號 parcel_id 和重量 weight。
建立 parcels 清單，只將重量不超過 3 公斤的包裹視為通過檢查，累加通過包裹的重量。
最後印出「通過檢查的包裹總重量：總重量 kg」。

標準輸入範例 1：

parcels = [Parcel("P001", 2.3), Parcel("P002", 4.8)]

預期輸出 1：

通過檢查的包裹總重量：2.3 kg

標準輸入範例 2：

parcels = [Parcel("P003", 1.5), Parcel("P004", 2.1)]

預期輸出 2：

通過檢查的包裹總重量：1.5 kg
'''