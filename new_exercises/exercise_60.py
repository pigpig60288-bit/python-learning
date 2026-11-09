'''
教學：清單可以保存多個物件。用 for 取出物件後，可以呼叫該物件的方法。

範例：
class Bell:
    def ring(self):
        print("叮咚")

bells = [Bell(), Bell()]
for bell in bells:
    bell.ring()
'''

'''
題目 60：讓多台機器回報狀態
定義 Machine 類別，在 __init__ 中儲存機器名稱 name 和狀態 status。
新增 show_status 方法，印出「名稱 狀態」。
建立 machines 清單並用 for 迴圈逐一呼叫每台機器的 show_status。

標準輸入範例 1：

machines = [Machine("A", "正常"), Machine("B", "故障")]

預期輸出 1：

A 正常\nB 故障

標準輸入範例 2：

machines = [Machine("C", "正常"), Machine("D", "故障")]

預期輸出 2：

C 正常\nD 故障
'''