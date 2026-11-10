'''
教學：更新物件狀態前，可以先判斷數值；若已經沒有需要處理的量，就不再扣減。

class Box:
    def __init__(self, items):
        self.items = items

class Mover:
    def take_one(self, box):
        if box.items > 0:
            box.items -= 1
            print("取出一件")
        else:
            print("箱子已空")

box = Box(1)
mover = Mover()
mover.take_one(box)

每次執行後都可以查看 box.items，確認狀態沒有變成不合理的數值。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 98：技師維修汽車

定義 Car 類別，儲存車名 name 和待修項目 damage。
定義 Mechanic 類別，儲存技師名稱 name 和完成的維修次數 repair_count，初始值為 0。

新增 repair 方法，接收一個 Car 物件：
- damage 大於 0 時，每次維修讓 damage 減少 1，repair_count 增加 1。
- damage 等於 0 時，顯示汽車不需要維修，兩個物件的數值都保持不變。
- 顯示維修結果、剩餘待修項目和技師完成的維修次數。

在 if __name__ == "__main__": 區塊建立物件並呼叫 repair。

標準輸入範例 1：

car = Car("小藍", 2)
mechanic = Mechanic("阿明")
mechanic.repair(car)

預期輸出 1：

維修完成一項
小藍剩餘待修 1 項
阿明完成維修 1 次

標準輸入範例 2：

car = Car("小白", 0)
mechanic = Mechanic("阿芳")
mechanic.repair(car)

預期輸出 2：

汽車不需要維修
小白剩餘待修 0 項
阿芳完成維修 0 次
'''
