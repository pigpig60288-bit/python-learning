'''
教學：一個物件的方法可以接收另一個物件，依對方的狀態做不同處理。

class Package:
    def __init__(self, delivered):
        self.delivered = delivered

class Courier:
    def deliver(self, package):
        if not package.delivered:
            package.delivered = True
            print("完成配送")
        else:
            print("已經配送過")

package = Package(False)
courier = Courier()
courier.deliver(package)

布林屬性可以放在 if 條件中，表示某件事目前是否完成。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 97：護理師照顧病患

定義 Patient 類別，儲存病患名稱 name 和目前體力 energy。
定義 Nurse 類別，儲存護理師名稱 name 和照顧人數 care_count，初始值為 0。

新增 care 方法，接收一個 Patient 物件：
- 每照顧一次，病患體力增加 3，護理師的 care_count 增加 1。
- 顯示病患目前體力及護理師照顧人數。

在 if __name__ == "__main__": 區塊建立物件並呼叫 care。

標準輸入範例 1：

patient = Patient("小雅", 10)
nurse = Nurse("王護理師")
nurse.care(patient)

預期輸出 1：

小雅目前體力 13
王護理師照顧 1 人

標準輸入範例 2：

patient = Patient("小凱", 6)
nurse = Nurse("李護理師")
nurse.care(patient)
nurse.care(patient)

預期輸出 2：

小凱目前體力 12
李護理師照顧 2 人
'''
