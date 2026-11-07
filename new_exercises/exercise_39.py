# 教學：方法除了 self，也可以接收其他參數。
# 呼叫時把資料放在括號裡，方法就能用這筆資料完成工作。
# 範例：
# class Instrument:
#     def __init__(self, name):
#         self.name = name
#
#     def play_song(self, song):
#         print(self.name + "演奏" + song)
#
# piano = Instrument("鋼琴")
# piano.play_song("小星星")
# song 參數接收呼叫時提供的曲名。
#
# 題目 39：為寵物準備食物
# 定義 Pet 類別，用 __init__ 儲存 name，並新增 feed 方法。
# feed 方法接收 food 參數，印出「○○吃了○○。」，
# 第一個○○是寵物名字，第二個○○是食物名稱。
# 建立一隻寵物，呼叫 feed 方法並傳入一種食物。
