# 教學：方法可同時使用物件自己的屬性和呼叫時收到的參數。
# 範例：
# class Card:
#     def __init__(self, color):
#         self.color = color
#
#     def describe(self, shape):
#         print(self.color + shape)
#
# card = Card("藍色")
# card.describe("圓形")
# color 來自物件，shape 則由呼叫方法時傳入。
#
# 題目 53：介紹寵物品種
# 定義 Pet 類別，使用 __init__ 儲存 name。
# 新增 introduce 方法，接收 kind 參數並印出寵物名字和品種。
# 建立一隻寵物並呼叫 introduce，傳入一種品種。
