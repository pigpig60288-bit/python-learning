'''
教學：定義在 class 裡的函式稱為方法。
方法的第一個參數通常寫 self，透過 self 可以讀取該物件自己的屬性。
範例：
class Instrument:
def __init__(self, name):
self.name = name
def play(self):
print(self.name + "正在演奏")
piano = Instrument("鋼琴")
piano.play()
呼叫 piano.play() 時，Python 會把 piano 傳給方法的 self。
'''

'''
題目 38：讓寵物自我介紹
定義 Pet 類別，用 __init__ 儲存 name，並新增 introduce 方法。
introduce 方法要印出「我是○○。」（○換成寵物名字）。
建立一隻名字為「小白」的寵物，呼叫它的 introduce 方法。
'''

class Pet:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"我是{self.name}。")
pet = Pet("小白")
pet.introduce()
