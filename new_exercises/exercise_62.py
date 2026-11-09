'''
教學：物件清單裡的每一項都能讀取自己的屬性；for 迴圈可逐項取得並印出。

範例：
class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

toys = [Toy("小熊", "棕色"), Toy("小兔", "白色")]
for toy in toys:
    print(f"{toy.name} 是 {toy.color}")
'''

'''
題目 62：列出收藏的書名
定義 Book 類別，在 __init__ 中儲存書名 name 和頁數 pages。
新增 show_info 方法，印出「書名 頁數」。
建立 books 清單並用 for 迴圈逐一呼叫每本書的 show_info。

標準輸入範例 1：

books = [Book("小王子", 120), Book("哈利波特", 350)]

預期輸出 1：

小王子 120\n哈利波特 350

標準輸入範例 2：

books = [Book("白雪公主", 90), Book("小鹿斑比", 70)]

預期輸出 2：

白雪公主 90\n小鹿斑比 70
'''