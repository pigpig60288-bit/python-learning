'''
教學：方法接收另一個物件後，可以先檢查它的屬性，再決定是否更新狀態。

class Locker:
    def __init__(self, available):
        self.available = available

class Student:
    def use_locker(self, locker):
        if locker.available:
            locker.available = False
            print("使用置物櫃")
        else:
            print("置物櫃已被使用")

locker = Locker(True)
student = Student()
student.use_locker(locker)

if 條件可以讀取另一個物件的屬性；條件成立時再更新該物件。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件及呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 93：玩家使用藥水

定義 Potion 類別，儲存藥水名稱 name、每次恢復的體力 restore_amount 和剩餘數量 count。
定義 Player 類別，儲存玩家名稱 name 和目前體力 energy。

新增 use_potion 方法，接收一個 Potion 物件：
- 藥水 count 大於 0 時，玩家體力增加 restore_amount，藥水 count 減少 1。
- 沒有藥水時，使用失敗，玩家體力和藥水數量都不變。
- 顯示使用結果、目前體力和藥水剩餘數量。

在 if __name__ == "__main__": 區塊建立物件並呼叫 use_potion。

標準輸入範例 1：

potion = Potion("活力藥水", 5, 2)
player = Player("阿哲", 10)
player.use_potion(potion)

預期輸出 1：

使用成功
阿哲目前體力 15
活力藥水剩餘 1 瓶

標準輸入範例 2：

potion = Potion("活力藥水", 5, 0)
player = Player("小文", 10)
player.use_potion(potion)

預期輸出 2：

使用失敗
小文目前體力 10
活力藥水剩餘 0 瓶
'''
