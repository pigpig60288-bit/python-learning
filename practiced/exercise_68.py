'''
教學：布林屬性可以直接放在 if 條件中，True 和 False 會走不同分支。

範例：
class Door:
    def __init__(self, is_locked):
        self.is_locked = is_locked

    def show_status(self):
        if self.is_locked:
            print("門已上鎖")
        else:
            print("門未上鎖")

door = Door(True)
door.show_status()
'''

'''
題目 68：找出可參加活動的隊員
定義 Member 類別，在 __init__ 中儲存隊員名稱 name 和是否符合參加資格 eligible。
新增 show_status 方法：eligible 為 True 時印出「名稱 可參加」，否則印出「名稱 不可參加」。
建立 members 清單並逐一呼叫每位隊員的 show_status。

標準輸入範例 1：

members = [Member("小白", True), Member("小明", False)]

預期輸出 1：

小白 可參加
小明 不可參加

標準輸入範例 2：

members = [Member("阿慶", True), Member("玲玲", True)]

預期輸出 2：

阿慶 可參加
玲玲 可參加
'''
class Member:
    def __init__(self, name, eligible):
        self.name = name
        self.eligible = eligible
    def show_status(self):
        if self.eligible == True:
            print(f"{self.name} 可參加")
        else:
            print(f"{self.name} 不可參加")

members = [Member("小白", True), Member("小明", False)]
for member in members:
    member.show_status()