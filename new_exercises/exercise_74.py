'''
教學：走訪物件清單時，可以用 if 比較每個物件的數字屬性，只處理符合條件的項目。

範例：
class Delivery:
    def __init__(self, zone, boxes):
        self.zone = zone
        self.boxes = boxes

deliveries = [Delivery("北區", 8), Delivery("南區", 3)]
for delivery in deliveries:
    if delivery.boxes >= 5:
        print(delivery.zone)
'''

'''
題目 74：計算達標的每日銷售量
定義 Sale 類別，在 __init__ 中儲存日期 day 和銷售量 amount。
建立 sales 清單並走訪其中的物件，只印出銷售量至少 100 的日期。
輸出格式為「達標的日子：日期」。

標準輸入範例 1：

sales = [Sale("週一", 120), Sale("週二", 90)]

預期輸出 1：

達標的日子：週一

標準輸入範例 2：

sales = [Sale("週三", 80), Sale("週四", 160)]

預期輸出 2：

達標的日子：週四
'''