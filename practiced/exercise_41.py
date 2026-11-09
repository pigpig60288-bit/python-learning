'''
教學：建立物件後，可以呼叫它的方法，讓物件執行一項工作。
方法寫在 class 裡，呼叫時使用「物件名稱.方法名稱()」。
範例：
class Lamp:
def turn_on(self):
print("燈亮了")
desk_lamp = Lamp()
desk_lamp.turn_on()
這會呼叫 desk_lamp 的 turn_on 方法。
'''

'''
題目 41：啟動機器人
定義 Robot 類別，新增一個 greet 方法，讓它印出啟動問候訊息。
建立一個 Robot 物件存入 my_robot，並呼叫它的 greet 方法一次。
執行程式時，確認問候訊息會出現。
'''

class Robot:
    def greet(self):
        print("您好")
my_robot = Robot()
my_robot.greet()
