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
題目 85：找出空閒且有設備的教室
定義 Classroom 類別，儲存教室名稱 name、是否空閒 is_available 和是否有設備 has_equipment。
新增 show_status 方法：兩個條件都為 True 時印出「名稱 可使用」；沒有設備時印出「名稱 設備不足」；不空閒時印出「名稱 不可使用」。
建立 classrooms 清單並逐一呼叫每個教室的 show_status。

標準輸入範例 1：

classrooms = [Classroom("A101", True, True), Classroom("B205", True, False)]

預期輸出 1：

A101 可使用\nB205 設備不足

標準輸入範例 2：

classrooms = [Classroom("C303", False, True), Classroom("D404", True, True)]

預期輸出 2：

C303 不可使用\nD404 可使用
'''