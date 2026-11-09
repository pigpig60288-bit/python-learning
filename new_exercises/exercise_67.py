'''
教學：for 迴圈可以逐一取出物件，再讀取其中的數字屬性並加入累加器。

範例：
class Package:
    def __init__(self, size):
        self.size = size

packages = [Package(3), Package(4)]
total_size = 0
for package in packages:
    total_size += package.size

print(total_size)
'''

'''
題目 67：計算書籍總頁數
定義 Book 類別，在 __init__ 中儲存書名 name 和頁數 pages。
建立 books 清單，用 for 迴圈逐一讀取每本書的 pages 並累加，最後印出總頁數。

標準輸入範例 1：

books = [Book("Python 入門", 120), Book("資料結構", 240)]

預期輸出 1：

總頁數：360

標準輸入範例 2：

books = [Book("美術史", 100), Book("世界地圖", 180)]

預期輸出 2：

總頁數：280
'''