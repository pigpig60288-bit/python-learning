'''
教學：for 和 while 可以分別負責不同工作

while 可以反覆收集資料並加入 list（清單）；資料收集完成後，for 可以逐項處理清單內容。

names = []
name = input("輸入名字，完成時輸入停止：")
while name != "停止":
    names.append(name)
    name = input("輸入名字，完成時輸入停止：")

for name in names:
    print(name)

上面的 while 負責收集，for 負責處理每一筆資料。
'''

'''
題目 104：照顧寵物

請將 Pet 類別放在 pet.py，Caretaker 類別放在 caretaker.py。
本題重點是不同類別互動：Caretaker 的 walk 方法要接收 Pet 物件，並更新該寵物的散步次數。
Pet 儲存寵物名稱 name 和散步次數 walk_count，初始散步次數為 0。
Caretaker 儲存照顧者名稱 name，並新增 walk(pet) 方法，讓指定寵物的 walk_count 增加 1。

在本檔案匯入兩個類別，建立寵物清單。
用 while 讀取寵物名稱，輸入「完成」時停止；每個名稱建立 Pet 物件並加入清單。
接著用 for 讓照顧者帶每隻寵物散步一次，再用另一個 for 顯示每隻寵物的散步次數。
主程式放在 if __name__ == "__main__": 區塊中。

標準輸入範例 1：

豆豆
球球
完成

已知資料：照顧者小美。

預期輸出 1：

豆豆散步 1 次
球球散步 1 次

標準輸入範例 2：

咪咪
完成

已知資料：照顧者小安。

預期輸出 2：

咪咪散步 1 次
'''
