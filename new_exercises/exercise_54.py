# 教學：方法可以用參數更新物件的數值屬性。
# 使用 += 把新數值加到物件原本保存的數值。
# 範例：
# class Jar:
#     def __init__(self):
#         self.marble_count = 0
#
#     def add_marbles(self, amount):
#         self.marble_count += amount
#
# jar = Jar()
# jar.add_marbles(4)
# print(jar.marble_count)
# 呼叫方法後，marble_count 會記住增加後的值。
#
# 題目 54：記錄游泳距離
# 定義 Swimmer 類別，__init__ 接收 name，並將 distance 設為 0。
# 新增 swim 方法，接收 distance 參數並累加到物件的 distance。
# 建立一位游泳者，呼叫 swim(3)，再印出 distance。
