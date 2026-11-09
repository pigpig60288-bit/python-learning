'''
教學：清單可以保存多個物件；for 迴圈每次會取出其中一個物件。
取出的物件可以像一般變數一樣呼叫自己的方法。
範例：
class Bell:
    def ring(self):
        print("鈴聲")

bells = [Bell(), Bell()]
for bell in bells:
    bell.ring()
迴圈會依序對清單中的每個 Bell 物件呼叫 ring。
'''

'''
題目 48：讓多隻寵物打招呼
定義 Pet 類別，新增 greet 方法，讓它印出一則打招呼訊息。
建立兩個 Pet 物件並放入 pets 清單。
使用 for 迴圈走訪 pets，對每個物件呼叫 greet。

標準輸入範例 1：
pets = [Pet("小白"), Pet("小黑")]

預期輸出 1：
小白 說：你好！
小黑 說：你好！

標準輸入範例 2：
pets = [Pet("阿明"), Pet("阿花")]

預期輸出 2：
阿明 說：你好！
阿花 說：你好！
'''

class Pet:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"{self.name} 說：你好！")

pets = [Pet("小白"), Pet("小黑")]
for pet in pets:
    pet.greet()
