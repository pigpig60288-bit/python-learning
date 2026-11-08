# 教學：物件的方法可以透過 self 讀取這個物件自己的屬性。
# 呼叫物件的方法時，Python 會自動把物件提供給 self。
# 範例：
# class Sign:
#     def __init__(self, word):
#         self.word = word
#
#     def show(self):
#         print(self.word)
#
# sign = Sign("入口")
# sign.show()
# show 方法會印出這個 Sign 物件保存的文字。
#
# 題目 51：顯示樂器名稱
# 定義 Instrument 類別，使用 __init__ 儲存 name。
# 新增 show_name 方法，印出物件的 name。
# 建立一個樂器物件並呼叫 show_name。
