'''
教學：先檢查另一個物件的狀態，再更新雙方屬性，可以避免重複執行動作。

class Seat:
    def __init__(self, occupied):
        self.occupied = occupied

class Visitor:
    def sit(self, seat):
        if not seat.occupied:
            seat.occupied = True
            print("坐下")
        else:
            print("座位已有人")

seat = Seat(False)
visitor = Visitor()
visitor.sit(seat)

呼叫方法後，請記得檢查 Seat 的狀態是否真的改變。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 96：乘客搭公車

定義 Passenger 類別，儲存乘客名稱 name 和是否已上車 boarded，初始值為 False。
定義 Bus 類別，儲存公車名稱 name 和剩餘座位 seats。

新增 board 方法，接收一個 Passenger 物件：
- seats 大於 0 且乘客尚未上車時，乘客成功上車，seats 減少 1，boarded 改為 True。
- 沒有空位或乘客已上車時，不改變公車和乘客的狀態。
- 顯示結果、公車剩餘座位，以及乘客是否已上車。

在 if __name__ == "__main__": 區塊建立物件並呼叫 board。

標準輸入範例 1：

bus = Bus("紅線公車", 2)
passenger = Passenger("小安")
bus.board(passenger)

預期輸出 1：

上車成功
紅線公車剩餘座位 1
小安已上車

標準輸入範例 2：

bus = Bus("藍線公車", 0)
passenger = Passenger("小庭")
bus.board(passenger)

預期輸出 2：

上車失敗
藍線公車剩餘座位 0
小庭尚未上車
'''
