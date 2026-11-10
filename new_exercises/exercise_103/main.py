'''
教學：清單可以保存自己建立的物件

建立物件後，可以用 append() 放進 list（清單），再用 for 逐一處理：

tools = []
tools.append("剪刀")
tools.append("膠水")

for tool in tools:
    print(tool)

while 迴圈可以讓使用者反覆輸入；搭配停止文字，就能決定何時結束收集。
'''

'''
題目 103：園丁照顧植物

請將 Plant 類別放在 plant.py，Gardener 類別放在 gardener.py。
本題重點是不同類別互動：Gardener 的 water 方法要接收 Plant 物件，並更新該植物的澆水次數。
Plant 儲存植物名稱 name 和澆水次數 water_count，初始澆水次數為 0。
Gardener 儲存園丁名稱 name，並新增 water(plant) 方法，讓指定植物的 water_count 增加 1。

在本檔案匯入兩個類別，建立一個植物清單。
使用 while 持續讀取植物名稱，輸入「完成」時停止；每個名稱建立一個 Plant 物件並加入清單。
之後使用 for 逐一呼叫園丁的 water 方法，並用 for 顯示每株植物的澆水次數。
主程式放在 if __name__ == "__main__": 區塊中。

標準輸入範例 1：

薄荷
蘭花
完成

已知資料：園丁阿青。

預期輸出 1：

薄荷澆水 1 次
蘭花澆水 1 次

標準輸入範例 2：

仙人掌
完成

已知資料：園丁小林。

預期輸出 2：

仙人掌澆水 1 次
'''
