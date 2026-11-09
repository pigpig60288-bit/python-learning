'''
教學：若只統計布林屬性為 True 的物件，可在 for 迴圈中用 if 和計數器。

範例：
class Lamp:
    def __init__(self, is_on):
        self.is_on = is_on

lamps = [Lamp(True), Lamp(False), Lamp(True)]
count = 0
for lamp in lamps:
    if lamp.is_on:
        count += 1

print(f"亮著的燈：{count}")
'''

'''
題目 88：統計已完成的課程
定義 Course 類別，在 __init__ 中儲存課程名稱 name 和完成狀態 is_done。
走訪 courses 清單，計算 is_done 為 True 的課程數量，最後印出「已完成課程：數量 門」。

標準輸入範例 1：

courses = [Course("數學", True), Course("英文", False)]

預期輸出 1：

已完成課程：1 門

標準輸入範例 2：

courses = [Course("歷史", True), Course("地理", True)]

預期輸出 2：

已完成課程：2 門
'''