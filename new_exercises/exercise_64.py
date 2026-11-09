'''
教學：可以在方法裡用 if/else 檢查物件的數量屬性，再印出不同結果。

範例：
class Locker:
    def __init__(self, items):
        self.items = items

    def check(self):
        if self.items > 0:
            print("置物櫃不是空的")
        else:
            print("置物櫃是空的")

locker = Locker(2)
locker.check()
'''

'''
題目 64：確認會員能否借書
定義 Member 類別，在 __init__ 中儲存會員名稱 name 和目前借閱本數 borrowed_count。
新增 check_borrow 方法：借閱本數大於 0 時印出「名稱 可以借書」，否則印出「名稱 不能借書」。
建立 Member 物件並呼叫 check_borrow。

標準輸入範例 1：

member = Member("小明", 2)

預期輸出 1：

小明 可以借書

標準輸入範例 2：

member = Member("阿美", 0)

預期輸出 2：

阿美 不能借書
'''