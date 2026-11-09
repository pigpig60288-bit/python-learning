'''
教學：這一題會練習把資料整理成物件，然後用條件控制處理邏輯。
每個物件可以存很多資訊，例如 name、score、stock、status 等屬性。
用 for 迴圈走訪清單時，可以依序取出每個物件，再用 if 判斷它是否符合條件。
如果符合條件，就更新資料、計算結果，或印出需要注意的內容。

範例：
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("小明", 90), Student("小華", 60)]
for student in students:
    if student.score >= 80:
        print(student.name)
'''

'''
題目 69：替低電量裝置充電
定義 Device 類別，在 __init__ 中儲存裝置名稱 name 和電量 level。
新增 show_status 方法：電量低於 20 時印出「名稱 需要充電」，否則印出「名稱 不需要充電」。
建立 devices 清單並逐一呼叫每個裝置的 show_status。

標準輸入範例 1：

devices = [Device("平板", 12), Device("電子書", 80)]

預期輸出 1：

平板 需要充電\n電子書 不需要充電

標準輸入範例 2：

devices = [Device("手機", 18), Device("耳機", 90)]

預期輸出 2：

手機 需要充電\n耳機 不需要充電
'''