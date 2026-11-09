'''
教學：and 表示兩個條件都成立。elif 可接著檢查其他狀況。

範例：
class Gate:
    def __init__(self, has_key, is_open):
        self.has_key = has_key
        self.is_open = is_open

    def show_status(self):
        if self.has_key and self.is_open:
            print("可以進入")
        elif self.is_open == False:
            print("門是關著的")
        else:
            print("需要鑰匙")

gate = Gate(True, True)
gate.show_status()
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