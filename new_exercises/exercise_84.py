'''
教學：分類計數時準備兩個計數器，再依每個物件的布林屬性增加其中一個。

範例：
class Light:
    def __init__(self, is_on):
        self.is_on = is_on

lights = [Light(True), Light(False), Light(True)]
on_count = 0
off_count = 0
for light in lights:
    if light.is_on:
        on_count += 1
    else:
        off_count += 1

print(on_count, off_count)
'''

'''
題目 84：統計課程完成狀態
定義 Course 類別，在 __init__ 中儲存課程名稱 name 和完成狀態 is_done。
走訪 courses 清單，分別統計已完成和未完成的課程數量。
輸出格式為「已完成：數量 門，未完成：數量 門」。

標準輸入範例 1：

courses = [Course("數學", True), Course("英文", False)]

預期輸出 1：

已完成：1 門，未完成：1 門

標準輸入範例 2：

courses = [Course("歷史", True), Course("地理", True)]

預期輸出 2：

已完成：2 門，未完成：0 門
'''