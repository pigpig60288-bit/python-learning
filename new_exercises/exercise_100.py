'''
教學：可以把另一個物件加入自己的清單，之後再走訪清單讀取每個物件的屬性。

class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def show_songs(self):
        for song in self.songs:
            print(song.title)

playlist = Playlist()
playlist.add_song(Song("海邊"))
playlist.show_songs()

add_song 收到一個 Song 物件後，將它加入 Playlist 的清單。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 100：訂單加入商品並計算總額

定義 Product 類別，儲存商品名稱 name 和價格 price。
定義 Order 類別，建立時準備一個空的 products 清單。

新增 add_product 方法，接收一個 Product 物件並將它加入 products 清單。
新增 show_total 方法，走訪 products 清單，計算並顯示訂單總額。
同一種商品可以加入多次；每次加入都要計入總額。

在 if __name__ == "__main__": 區塊建立商品和訂單物件，加入商品後呼叫 show_total。

標準輸入範例 1：

order = Order()
order.add_product(Product("筆記本", 25))
order.add_product(Product("橡皮擦", 10))
order.show_total()

預期輸出 1：

訂單總額 35 元

標準輸入範例 2：

order = Order()
order.add_product(Product("色紙", 15))
order.add_product(Product("色紙", 15))
order.add_product(Product("剪刀", 40))
order.show_total()

預期輸出 2：

訂單總額 70 元
'''
