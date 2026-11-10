'''
教學：方法可以接收另一個物件，並更新它的數值屬性。

class Plant:
    def __init__(self, height):
        self.height = height

class Gardener:
    def help_grow(self, plant):
        plant.height += 2

plant = Plant(4)
gardener = Gardener()
gardener.help_grow(plant)
print(plant.height)

這裡 Gardener 的方法接收 Plant 物件，並增加該物件的 height。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 94：教練訓練選手

定義 Athlete 類別，儲存選手名稱 name 和分數 score。
定義 Coach 類別，儲存教練名稱 name 和訓練次數 training_count，初始值為 0。

新增 train 方法，接收一個 Athlete 物件：
- 每訓練一次，選手的 score 增加 5，教練的 training_count 增加 1。
- 顯示選手名稱、目前分數及教練訓練次數。

在 if __name__ == "__main__": 區塊建立 Coach 和 Athlete 物件並呼叫 train。

標準輸入範例 1：

coach = Coach("林教練")
athlete = Athlete("小偉", 20)
coach.train(athlete)

預期輸出 1：

小偉目前分數 25
林教練訓練 1 次

標準輸入範例 2：

coach = Coach("陳教練")
athlete = Athlete("小晴", 30)
coach.train(athlete)
coach.train(athlete)

預期輸出 2：

小晴目前分數 40
陳教練訓練 2 次
'''
