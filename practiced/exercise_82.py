'''
教學：用 for 走訪物件清單，再以 if 篩選符合條件的資料並印出識別資訊。

範例：
class Package:
    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

packages = [Package("X1", 6), Package("X2", 2)]
for package in packages:
    if package.weight >= 5:
        print(package.code)
'''

'''
題目 82：統計金額達標的訂單
定義 Order 類別，在 __init__ 中儲存訂單編號 order_id 和金額 amount。
建立 orders 清單，只列出金額至少 400 元的訂單編號。
輸出格式為「金額達標的訂單：訂單編號」。

標準輸入範例 1：

orders = [Order("A001", 450), Order("A002", 280)]

預期輸出 1：

金額達標的訂單：A001

標準輸入範例 2：

orders = [Order("B001", 350), Order("B002", 520)]

預期輸出 2：

金額達標的訂單：B002
'''
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

orders = [Order("A001", 450), Order("A002", 280)]
for order in orders:
    if order.amount >= 400:
        print(f"金額達標的訂單：{order.order_id}")