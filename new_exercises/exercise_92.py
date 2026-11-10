'''
教學：一個物件的方法可以接收另一個物件，並更新對方的屬性。

class Lamp:
    def __init__(self, is_on):
        self.is_on = is_on

class Switch:
    def turn_on(self, lamp):
        lamp.is_on = True

lamp = Lamp(False)
switch = Switch()
switch.turn_on(lamp)
print(lamp.is_on)

呼叫 turn_on(lamp) 後，方法中的 lamp 代表傳入的 Lamp 物件，因此更新它的 is_on。
直接執行檔案時，__name__ 會是 "__main__"。把建立物件及呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 92：會員借書

定義 Book 類別，儲存書名 title 和可借數量 copies。
定義 LibraryMember 類別，儲存會員名稱 name 和已借書本數 borrowed_count，初始值為 0。

新增 borrow 方法，接收一個 Book 物件：
- copies 大於 0 時，借書成功，copies 減少 1，會員的 borrowed_count 增加 1。
- copies 等於 0 時，借書失敗，兩個物件的數值都保持不變。
- 顯示借閱結果、目前可借數量和會員已借書本數。

在 if __name__ == "__main__": 區塊建立物件並呼叫 borrow。

標準輸入範例 1：

book = Book("海洋故事", 2)
member = LibraryMember("小庭")
member.borrow(book)

預期輸出 1：

借閱成功
海洋故事目前可借 1 本
小庭已借 1 本

標準輸入範例 2：

book = Book("森林故事", 0)
member = LibraryMember("小宇")
member.borrow(book)

預期輸出 2：

借閱失敗
森林故事目前可借 0 本
小宇已借 0 本
'''
