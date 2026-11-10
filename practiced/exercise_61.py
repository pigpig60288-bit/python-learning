'''
教學：方法可以在物件清單中逐一呼叫；方法裡用 if/else 依數值屬性選擇訊息。

範例：
class Plant:
    def __init__(self, moisture):
        self.moisture = moisture

    def show_status(self):
        if self.moisture < 30:
            print("土壤乾燥")
        else:
            print("土壤濕潤")

plants = [Plant(20), Plant(45)]
for plant in plants:
    plant.show_status()
'''

'''
題目 61：列出需要充電的裝置
定義 Device 類別，在 __init__ 中儲存裝置名稱 name 和電量 level。
新增 show_status 方法：電量低於 20 時印出「名稱 需要充電」，否則印出「名稱 已充電」。
建立 devices 清單並逐一呼叫每個裝置的 show_status。

標準輸入範例 1：

devices = [Device("手機", 15), Device("平板", 22)]

預期輸出 1：

手機 需要充電\n平板 已充電

標準輸入範例 2：

devices = [Device("筆電", 30), Device("耳機", 12)]

預期輸出 2：

筆電 已充電\n耳機 需要充電
'''
class Device:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def show_status(self):
        if self.level < 20:
            print(f"{self.name}需要充電")
        else:
            print(f"{self.name}已充電")

devices = [Device("手機", 15), Device("平板", 22)]
for device in devices:
    device.show_status()