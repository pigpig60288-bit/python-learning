'''
教學：物件可以用多個屬性保存相關資料，方法可以用 f-string 顯示這些屬性。
__init__ 的參數會在建立物件時提供；self.attribute 會把資料存進物件。

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
題目 52：記錄電影資料
定義 Movie 類別，並在 __init__ 中儲存電影名稱 name 和上映年份 year。
新增 show_info 方法，印出「電影：名稱（年份）」。建立 Movie 物件後呼叫這個方法。

標準輸入範例 1：

movie = Movie("星際大戰", 2024)

預期輸出 1：

電影：星際大戰（2024）

標準輸入範例 2：

movie = Movie("阿凡達", 2009)

預期輸出 2：

電影：阿凡達（2009）
'''
class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def show_info(self):
        print(f"電影：{self.name}({self.year})")
movie = Movie("阿凡達", 2009)
movie.show_info()