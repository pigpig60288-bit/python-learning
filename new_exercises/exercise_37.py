# 教學：__init__ 是建立物件時自動執行的初始化方法。
# self 代表目前正在建立或使用的那個物件。
# 把傳入的資料存到 self.name，物件就能保留自己的 name。
# 範例：
# class Instrument:
#     def __init__(self, name):
#         self.name = name
#
# piano = Instrument("鋼琴")
# print(piano.name)
# 建立 piano 時，"鋼琴" 會存入這個物件的 name 屬性。
#
# 題目 37：建立寵物資料
# 定義 Pet 類別，使用 __init__ 接收一個 name，並存入物件的 self.name。
# 建立一個名字為「小白」的 Pet 物件，印出它的 name。
