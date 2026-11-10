'''
教學：方法可以修改物件自己的數值屬性。使用 += 會把新數值加到原本的值上。

範例：
class Plant:
    def __init__(self, name):
        self.name = name
        self.water = 0

    def add_water(self, amount):
        self.water += amount

plant = Plant("薄荷")
plant.add_water(2)
print(plant.water)
'''

'''
題目 54：記錄游泳距離
定義 Swimmer 類別，在 __init__ 中儲存名字 name，並將游泳距離 distance 設為 0。
新增 add_distance 方法，接收距離並累加到 distance；再新增 show_distance 方法印出目前總距離。
建立 Swimmer 物件後，依範例呼叫 add_distance，再呼叫 show_distance。

標準輸入範例 1：

swimmer = Swimmer("小安")
swimmer.add_distance(8)
swimmer.show_distance()

預期輸出 1：

游泳距離：8

標準輸入範例 2：

swimmer = Swimmer("阿傑")
swimmer.add_distance(6)
swimmer.show_distance()

預期輸出 2：

游泳距離：6
'''
class Swimmer:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def add_distance(self, amount):
        self.distance += amount

    def show_distance(self):
        print(f"游泳距離:{self.distance}")

swimmer = Swimmer("阿毛")
swimmer.add_distance(5)
swimmer.show_distance()