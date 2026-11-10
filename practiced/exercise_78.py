'''
教學：布林屬性可用 if/else 分成兩種狀態，再用方法印出對應文字。

範例：
class Door:
    def __init__(self, is_locked):
        self.is_locked = is_locked

    def show_status(self):
        if self.is_locked:
            print("門已上鎖")
        else:
            print("門未上鎖")

door = Door(False)
door.show_status()
'''

'''
題目 78：統計完成與未完成任務
定義 Task 類別，在 __init__ 中儲存任務名稱 name 和完成狀態 is_done。
新增 show_status 方法：依 is_done 印出「任務名稱 已完成」或「任務名稱 未完成」。
建立 tasks 清單並逐一呼叫每個任務的 show_status。

標準輸入範例 1：

tasks = [Task("整理資料", True), Task("回覆信件", False)]

預期輸出 1：

整理資料 已完成
回覆信件 未完成

標準輸入範例 2：

tasks = [Task("讀書", True), Task("打掃", True)]

預期輸出 2：

讀書 已完成
打掃 已完成
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

tasks = [Task("整理資料", True), Task("回覆信件", False)]
for task in tasks:
    task.show_status()