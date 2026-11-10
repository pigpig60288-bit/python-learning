'''
教學：把名稱與布林狀態放在物件中，方法可用 if/else 顯示文字狀態。

範例：
class Door:
    def __init__(self, name, is_open):
        self.name = name
        self.is_open = is_open

    def show_status(self):
        if self.is_open:
            print(f"{self.name} 開著")
        else:
            print(f"{self.name} 關著")

door = Door("後門", True)
door.show_status()
'''

'''
題目 83：管理每日任務
定義 Task 類別，在 __init__ 中儲存任務名稱 name 和完成狀態 is_done。
新增 show_status 方法，依完成狀態印出「任務名稱 已完成」或「任務名稱 未完成」。
建立 tasks 清單並逐一呼叫每個任務的 show_status。

標準輸入範例 1：

tasks = [Task("閱讀", True), Task("運動", False)]

預期輸出 1：

閱讀 已完成
運動 未完成

標準輸入範例 2：

tasks = [Task("打掃", True), Task("整理", True)]

預期輸出 2：

打掃 已完成
整理 已完成
'''
class Task:
    def __init__(self, name, is_done):
        self.name = name
        self.is_done = is_done

    def show_status(self):
        if self.is_done:
            print(f"{self.name} 已完成")
        else:
            print(f"{self.name} 未完成")

tasks = [Task("閱讀", True), Task("運動", False)]
for task in tasks:
    task.show_status()