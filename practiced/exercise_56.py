'''
教學：物件能保存數量屬性，方法可以比較屬性和門檻，再用 f-string 顯示結果。

範例：
class Box:
    def __init__(self, count):
        self.count = count

    def check(self):
        if self.count >= 4:
            print(f"盒子裡有 {self.count} 顆")
        else:
            print("數量還不夠")

box = Box(6)
box.check()
'''

'''
題目 56：檢查座位是否足夠
定義 Classroom 類別，依序儲存教室名稱、座位總數和空位數。
新增 check_seats 方法：空位至少 5 個時印出座位足夠，否則印出座位不足；訊息中也要顯示空位數。
建立 Classroom 物件並呼叫 check_seats。

標準輸入範例 1：

classroom = Classroom("A101", 8, 6)

預期輸出 1：

座位足夠：6 個空位

標準輸入範例 2：

classroom = Classroom("B205", 5, 2)

預期輸出 2：

座位不足：2 個空位
'''
class Classroom:
    def __init__(self, name, all, seat):
        self.name = name
        self.all = all
        self.seat = seat

    def check_seats(self):
        if self.seat >= 5:
            print(f"座位足夠：{self.seat}個空位")
        else:
            print(f"座位不足：{self.seat}個空位")
classroom = Classroom("H101", 10, 4)
classroom.check_seats()