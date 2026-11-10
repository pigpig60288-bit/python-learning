'''
教學：若數值放在物件屬性中，可以在 for 迴圈裡逐一讀取並用 += 累加。

範例：
class Parcel:
    def __init__(self, weight):
        self.weight = weight

parcels = [Parcel(2), Parcel(5)]
total = 0
for parcel in parcels:
    total += parcel.weight

print(total)
'''

'''
題目 63：增加花盆中的花朵數
定義 Flower 類別，在 __init__ 中儲存花朵數量 count。
建立 flowers 清單，用 for 迴圈走訪每個 Flower 物件並累加 count，最後印出總花朵數。

標準輸入範例 1：

flowers = [Flower(2), Flower(5), Flower(1)]

預期輸出 1：

總花朵數：8

標準輸入範例 2：

flowers = [Flower(4), Flower(3)]

預期輸出 2：

總花朵數：7
'''
class Flower:
    def __init__(self, count):
        self.count = count

flowers = [Flower(2), Flower(5), Flower(1)]
total = 0
for flower in flowers:
    total += flower.count

print(f"總花朵數：{total}")