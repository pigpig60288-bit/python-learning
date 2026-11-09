'''
教學：sort(key=...) 可指定物件排序依據。lambda 是簡短函式；此處會從每本書取出 pages 作為排序值。

範例：
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

books = [Book("地圖集", 80), Book("植物百科", 120)]
books.sort(key=lambda book: book.pages)

for book in books:
    print(book.title, book.pages)
'''

'''
題目 77：排列測驗分數
定義 Score 類別，在 __init__ 中儲存學生姓名 name 和分數 score。
建立 scores 清單，依分數由低到高排列，然後逐一印出「姓名 分數」。

標準輸入範例 1：

scores = [Score("小美", 87), Score("小華", 56)]

預期輸出 1：

小華 56\n小美 87

標準輸入範例 2：

scores = [Score("琪琪", 92), Score("大宇", 68)]

預期輸出 2：

大宇 68\n琪琪 92
'''