'''
教學：在方法中檢查布林屬性，可以說明物件目前是哪一種狀態。

範例：
class Seat:
    def __init__(self, is_taken):
        self.is_taken = is_taken

    def show_status(self):
        if self.is_taken:
            print("座位有人")
        else:
            print("座位空著")

seat = Seat(False)
seat.show_status()
'''

'''
題目 79：避免重複加入收藏景點
定義 Spot 類別，在 __init__ 中儲存景點名稱 name 和是否已收藏 is_favorite。
新增 show_status 方法：已收藏時印出「名稱 已收藏」，否則印出「名稱 可加入收藏」。
建立 spots 清單並逐一呼叫每個景點的 show_status。

標準輸入範例 1：

spots = [Spot("日月潭", False), Spot("九份", True)]

預期輸出 1：

日月潭 可加入收藏
九份 已收藏

標準輸入範例 2：

spots = [Spot("墾丁", True), Spot("阿里山", False)]

預期輸出 2：

墾丁 已收藏
阿里山 可加入收藏
'''
class Spot:
    def __init__(self, name, is_favorite):
        self.name = name
        self.is_favorite = is_favorite

    def show_status(self):
        if self.is_favorite:
            print(f"{self.name} 已收藏")
        else:
            print(f"{self.name} 可加入收藏")

spots = [Spot("日月潭", False), Spot("九份", True)]
for spot in spots:
    spot.show_status()