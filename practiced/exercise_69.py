'''
教學：用比較運算子檢查數字屬性是否低於門檻，再以 if/else 選擇訊息。

範例：
class Room:
    def __init__(self, temperature):
        self.temperature = temperature

    def show_status(self):
        if self.temperature < 18:
            print("房間偏冷")
        else:
            print("溫度舒適")

room = Room(16)
room.show_status()
'''

'''
題目 69：替低電量裝置充電
定義 Device 類別，在 __init__ 中儲存裝置名稱 name 和電量 level。
新增 show_status 方法：電量低於 20 時印出「名稱 需要充電」，否則印出「名稱 不需要充電」。
建立 devices 清單並逐一呼叫每個裝置的 show_status。

標準輸入範例 1：

devices = [Device("平板", 12), Device("電子書", 80)]

預期輸出 1：

平板 需要充電
電子書 不需要充電

標準輸入範例 2：

devices = [Device("手機", 18), Device("耳機", 90)]

預期輸出 2：

手機 需要充電
耳機 不需要充電
'''
class Device:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_status(self):
        if self.level < 20:
            print(f"{self.name} 需要充電")
        else:
            print(f"{self.name} 不需要充電")

devices = [Device("平板", 12), Device("電子書", 80)]
for device in devices:
    device.show_status()