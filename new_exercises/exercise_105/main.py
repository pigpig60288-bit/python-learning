'''
教學：把不同類別的物件放進清單並使用方法

list（清單）可以保存物件，for 迴圈可以逐一呼叫每個物件的方法：

class Clock:
    def show(self):
        print("時間到了")

clocks = [Clock(), Clock()]
for clock in clocks:
    clock.show()

while 迴圈也可以讓使用者重複選擇要處理的資料，直到輸入停止文字。
'''

'''
題目 105：教練訓練選手

請將 Athlete 類別放在 athlete.py，Coach 類別放在 coach.py。
本題重點是不同類別互動：Coach 的 train 方法要接收 Athlete 物件，並更新該選手的訓練次數。
Athlete 儲存選手名稱 name 和訓練次數 training_count，初始訓練次數為 0。
Coach 儲存教練名稱 name，並新增 train(athlete) 方法，讓指定選手的 training_count 增加 1。

在本檔案匯入兩個類別，建立選手清單。
用 while 讀取選手名稱，輸入「完成」時停止；每個名稱建立 Athlete 物件並加入清單。
接著用 for 讓教練訓練清單中的每位選手一次，最後再用 for 顯示每位選手的訓練次數。
主程式放在 if __name__ == "__main__": 區塊中。

標準輸入範例 1：

小偉
小晴
完成

已知資料：教練林教練。

預期輸出 1：

小偉訓練 1 次
小晴訓練 1 次

標準輸入範例 2：

小宇
完成

已知資料：教練陳教練。

預期輸出 2：

小宇訓練 1 次
'''
