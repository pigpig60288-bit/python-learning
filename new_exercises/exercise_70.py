'''
教學：>= 表示「大於或等於」。走訪物件清單時可以檢查每個物件的數字屬性。

範例：
class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

players = [Player("小安", 12), Player("小文", 7)]
for player in players:
    if player.points >= 10:
        print(f"{player.name} 達標")
'''

'''
題目 70：計算已完成作業的分數
定義 Grade 類別，在 __init__ 中儲存學生姓名 name 和分數 score。
新增 show_status 方法：分數至少 80 分時印出「姓名 已完成」，否則印出「姓名 未完成」。
建立 homework 清單並逐一呼叫每個 Grade 物件的 show_status。

標準輸入範例 1：

homework = [Grade("小華", 88), Grade("小美", 70)]

預期輸出 1：

小華 已完成\n小美 未完成

標準輸入範例 2：

homework = [Grade("阿強", 95), Grade("志明", 60)]

預期輸出 2：
阿強 已完成\n志明 未完成
'''