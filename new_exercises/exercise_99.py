'''
教學：使用布林屬性記錄完成狀態，可以避免同一件事被重複計算。

class Task:
    def __init__(self, done):
        self.done = done

class Worker:
    def finish(self, task):
        if not task.done:
            task.done = True
            print("完成任務")
        else:
            print("任務早已完成")

task = Task(False)
worker = Worker()
worker.finish(task)

這裡先檢查 task.done，再決定是否把狀態改成 True。

直接執行檔案時，__name__ 會是 "__main__"。把建立物件和呼叫方法放在這個區塊中：

if __name__ == "__main__":
    print("開始執行")
'''

'''
題目 99：司機配送包裹

定義 Package 類別，儲存包裹編號 code 和是否已送達 delivered，初始值為 False。
定義 DeliveryDriver 類別，儲存司機名稱 name 和配送成功件數 delivery_count，初始值為 0。

新增 deliver 方法，接收一個 Package 物件：
- 包裹尚未送達時，將 delivered 改為 True，並讓 delivery_count 增加 1。
- 包裹已送達時，不重複增加 delivery_count。
- 顯示配送結果、包裹送達狀態及司機配送成功件數。

在 if __name__ == "__main__": 區塊建立物件並呼叫 deliver。

標準輸入範例 1：

package = Package("P101", False)
driver = DeliveryDriver("小陳")
driver.deliver(package)

預期輸出 1：

配送成功
包裹 P101 已送達
小陳配送成功 1 件

標準輸入範例 2：

package = Package("P202", True)
driver = DeliveryDriver("小林")
driver.deliver(package)

預期輸出 2：

包裹已送達，不重複計算
包裹 P202 已送達
小林配送成功 0 件
'''
