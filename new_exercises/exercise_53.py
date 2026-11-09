'''
教學：這一題會用到物件、清單與條件判斷。
先把資料放進物件裡，再把物件存進清單，最後用 for 迴圈逐一取出。
當你拿到某個物件時，可以用 if 檢查它的屬性，確認它是否符合條件。
只有符合條件的物件才該被修改、計算或印出結果。

範例：
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

items = [Product("杯子", 3), Product("筆記本", 7)]
for item in items:
    if item.stock < 5:
        print(item.name)
'''

'''
題目 53：介紹寵物品種
定義 Pet 類別，並在 __init__ 中儲存寵物名稱 name。
新增 introduce 方法，使用方法參數接收品種，並印出「名稱 是 品種」。
建立 Pet 物件後呼叫 introduce，將範例中的品種傳給方法。

標準輸入範例 1：

pet = Pet("旺財")
pet.introduce("貓")

預期輸出 1：

旺財 是 貓

標準輸入範例 2：

pet = Pet("米豆")
pet.introduce("狗")

預期輸出 2：

米豆 是 狗
'''