'''
教學一：__main__ 是程式直接執行時的入口

把主要要執行的程式放在這個判斷式下面：

def say_hello():
    print("你好")

if __name__ == "__main__":
    say_hello()

直接執行這個 Python 檔案時，__name__ 的值會是 "__main__"，所以會呼叫 say_hello()。
如果這個檔案被其他檔案匯入，裡面的函式可以被使用，但這個區塊不會自動執行。

教學二：讓不同類別的物件互相合作

方法可以把另一個物件當作參數。收到物件後，就能讀取或更新它的屬性。

class Plant:
    def __init__(self, name, water):
        self.name = name
        self.water = water

class Gardener:
    def water_plant(self, plant):
        plant.water += 1
        print(f"{plant.name} 的水量增加了")

if __name__ == "__main__":
    plant = Plant("薄荷", 2)
    gardener = Gardener()
    gardener.water_plant(plant)

呼叫 water_plant(plant) 時，plant 物件會傳進方法；方法更新的是那個 Plant 物件的 water 屬性。
'''

'''
題目 91：顧客購買商品

定義 Product 類別，建立商品物件時儲存商品名稱 name、價格 price 和庫存 stock。
定義 Customer 類別，建立顧客物件時儲存顧客名稱 name 和持有金額 money。

在 Customer 類別中新增 buy 方法，讓它接收一個 Product 物件：
- 只有顧客的 money 足以支付商品 price，而且商品 stock 大於 0 時，才能購買。
- 購買成功後，顧客的 money 減少商品價格，商品的 stock 減少 1。
- 若金額不足或商品沒有庫存，購買失敗，顧客金額和商品庫存都保持不變。
- 無論購買成功或失敗，都顯示結果，以及顧客目前金額和商品目前庫存。

在 if __name__ == "__main__": 區塊中建立 Product 和 Customer 物件，並呼叫顧客的 buy 方法。
請用下列兩組資料分別測試；可以修改 main 區塊中的初始資料再執行。

標準輸入範例 1：

product = Product("餅乾", 30, 2)
customer = Customer("小安", 100)
customer.buy(product)

預期輸出 1：

購買成功，商品是餅乾
小安目前金額 70
餅乾目前庫存 1

標準輸入範例 2：

product = Product("果汁", 50, 2)
customer = Customer("小晴", 20)
customer.buy(product)

預期輸出 2：

購買失敗，原因是金額不足
小晴目前金額 20
果汁目前庫存 2
'''
