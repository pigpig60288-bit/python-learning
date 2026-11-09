'''
教學：方法除了 self，也可以有自己的參數。呼叫方法時，括號內的值會傳給該參數。

範例：
class Greeter:
    def __init__(self, name):
        self.name = name

    def say_hello(self, place):
        print(f"{self.name} 在 {place} 向大家問好")

greeter = Greeter("小林")
greeter.say_hello("公園")
'''

'''
題目 53：介紹寵物品種
定義 Pet 類別，並在 __init__ 中儲存寵物名稱 name。
新增 introduce 方法，使用方法參數接收品種，並印出「名稱 是 品種」。
建立 Pet 物件後呼叫 introduce，將範例中的品種傳給方法。

標準輸入範例 1：

pet = Pet("旺財")
pet.introduce("貓")

預期輸出 1：

旺財 是 貓

標準輸入範例 2：

pet = Pet("米豆")
pet.introduce("狗")

預期輸出 2：

米豆 是 狗
'''