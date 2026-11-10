'''
教學：可先用 if 篩選符合條件的物件，再將它的數字屬性加到累加器。

範例：
class Package:
    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

packages = [Package("X1", 2), Package("X2", 5)]
total = 0
for package in packages:
    if package.weight <= 3:
        total += package.weight

print(total)
'''

'''
題目 89：計算通過檢查的包裹總重量
定義 Parcel 類別，在 __init__ 中儲存包裹編號 parcel_id 和重量 weight。
建立 parcels 清單，只將重量不超過 3 公斤的包裹視為通過檢查，累加通過包裹的重量。
最後印出「通過檢查的包裹總重量：總重量 kg」。

標準輸入範例 1：

parcels = [Parcel("P001", 2.3), Parcel("P002", 4.8)]

預期輸出 1：

通過檢查的包裹總重量：2.3 kg

標準輸入範例 2：

parcels = [Parcel("P003", 1.5), Parcel("P004", 2.1)]

預期輸出 2：

通過檢查的包裹總重量：1.5 kg
'''

class Parcel:
    def __init__(self, parcel_id, weight):
        self.parcel_id = parcel_id
        self.weight = weight

parcels = [Parcel("P001", 2.3), Parcel("P002", 4.8)]
total = 0
for parcel in parcels:
    if parcel.weight <= 3:
        total += parcel.weight
        print(f"通過檢查的包裹總重量：{total}")