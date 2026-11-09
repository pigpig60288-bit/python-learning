'''
教學：方法參數可以控制是否更新物件屬性。條件成立時才用 += 增加數值。

範例：
class Shelf:
    def __init__(self):
        self.books = 0

    def add_books(self, amount, is_open):
        if is_open:
            self.books += amount

shelf = Shelf()
shelf.add_books(3, True)
print(shelf.books)
'''

'''
題目 72：只有營業時才能增加來客數
定義 Customer 類別，儲存顧客名稱 name 和來客數 count，初始來客數設為 0。
新增 add_customers 方法，接收增加數量 amount 和營業狀態 is_open；只有 is_open 為 True 時才增加 count。
建立 customers 清單並呼叫方法，再逐一印出每位顧客的來客數。

標準輸入範例 1：

customers = [Customer("小青", 0), Customer("小陳", 0)]
customers[0].add_customers(20, True)
customers[1].add_customers(5, True)

預期輸出 1：

小青 來客數：20\n小陳 來客數：5

標準輸入範例 2：

customers = [Customer("小美", 0), Customer("大文", 0)]
customers[0].add_customers(10, True)
customers[1].add_customers(15, False)

預期輸出 2：

小美 來客數：10\n大文 來客數：0
'''