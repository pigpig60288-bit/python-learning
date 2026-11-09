'''
教學：物件可儲存布林狀態。方法用 if/else 依 True 或 False 顯示相應訊息。

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
題目 73：記錄並檢查參加者
定義 Participant 類別，在 __init__ 中儲存參加者姓名 name 和是否已參加 attended。
新增 show_status 方法：attended 為 True 時印出「姓名 已參加」，否則印出「姓名 未參加」。
建立 participants 清單並逐一呼叫每個物件的 show_status。

標準輸入範例 1：

participants = [Participant("小榮", True), Participant("小文", False)]

預期輸出 1：

小榮 已參加\n小文 未參加

標準輸入範例 2：

participants = [Participant("阿傑", True), Participant("依依", True)]

預期輸出 2：

阿傑 已參加\n依依 已參加
'''