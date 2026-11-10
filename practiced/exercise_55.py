'''
教學：方法可以用 if/else 檢查物件屬性，並依條件選擇不同的輸出。

範例：
class Plant:
    def __init__(self, water):
        self.water = water

    def check_water(self):
        if self.water < 3:
            print("需要澆水")
        else:
            print("水分足夠")

plant = Plant(2)
plant.check_water()
'''

'''
題目 55：檢查電池電量
定義 Battery 類別，使用 __init__ 儲存電量 level。
新增 check_level 方法：電量低於 20 時印出「電量偏低」，否則印出「電量足夠」。
建立 Battery 物件並呼叫 check_level。

標準輸入範例 1：

battery = Battery(15)

預期輸出 1：

電量偏低

標準輸入範例 2：

battery = Battery(80)

預期輸出 2：

電量足夠
'''
class Battery:
    def __init__(self, level):
        self.level = level

    def check_level(self):
        if self.level < 20:
            print("電量偏低")
        else:
            print("電量足夠")

battery = Battery(65)
battery.check_level()