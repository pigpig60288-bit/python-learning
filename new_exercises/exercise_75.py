'''
教學：用 for 逐一檢查物件屬性，條件成立時才輸出該物件的資料。

範例：
class Visit:
    def __init__(self, place, hours):
        self.place = place
        self.hours = hours

visits = [Visit("博物館", 3), Visit("公園", 1)]
for visit in visits:
    if visit.hours >= 2:
        print(f"{visit.place}：{visit.hours} 小時")
'''

'''
題目 75：列出長時間的交通路線
定義 Route 類別，在 __init__ 中儲存路線名稱 name 和行車時間 minutes。
建立 routes 清單，只顯示行車時間至少 20 分鐘的路線，並印出「名稱：時間 分鐘」。
使用 for 迴圈逐一檢查路線。

標準輸入範例 1：

routes = [Route("台北", 35), Route("桃園", 20)]

預期輸出 1：

台北：35 分鐘\n桃園：20 分鐘

標準輸入範例 2：

routes = [Route("高雄", 45), Route("台中", 30)]

預期輸出 2：

高雄：45 分鐘\n台中：30 分鐘
'''