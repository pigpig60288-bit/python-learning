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
題目 83：管理每日任務
定義 Task 類別，在 __init__ 中儲存任務名稱 name 和完成狀態 is_done。
新增 show_status 方法，依完成狀態印出「任務名稱 已完成」或「任務名稱 未完成」。
建立 tasks 清單並逐一呼叫每個任務的 show_status。

標準輸入範例 1：

tasks = [Task("閱讀", True), Task("運動", False)]

預期輸出 1：

閱讀 已完成\n運動 未完成

標準輸入範例 2：

tasks = [Task("打掃", True), Task("整理", True)]

預期輸出 2：

打掃 已完成\n整理 已完成
'''