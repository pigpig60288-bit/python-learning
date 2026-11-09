'''
教學：物件可以用屬性保存文字和數字，方法可以用 f-string 顯示它們。

範例：
class Game:
    def __init__(self, title, players):
        self.title = title
        self.players = players

    def show_info(self):
        print(f"{self.title}，玩家人數：{self.players}")

game = Game("星球探險", 4)
game.show_info()
'''

'''
題目 71：顯示餐點資訊
定義 Meal 類別，在 __init__ 中儲存餐點名稱 name 和價格 price。
新增 show_info 方法，印出「餐點名稱：價格 元」。建立 Meal 物件後呼叫此方法。

標準輸入範例 1：

meal = Meal("漢堡", 120)

預期輸出 1：

漢堡：120 元

標準輸入範例 2：

meal = Meal("雞腿飯", 150)

預期輸出 2：

雞腿飯：150 元
'''