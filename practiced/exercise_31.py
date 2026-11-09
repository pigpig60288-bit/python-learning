'''
複習教學：input() 取得的內容是文字；要做數學計算時，使用 int() 轉成整數。
while 可以重複詢問，直到輸入指定的停止文字。
list 的 append() 可把資料加入清單；也可以用變數逐步累加總數。
範例：
books = []
pages_total = 0
title = input("輸入書名，輸入「好了」結束：")
while title != "好了":
books.append(title)
pages_total = pages_total + 10
title = input("輸入書名，輸入「好了」結束：")
這個例子用書名清單記錄資料，並累加頁數；題目會使用不同情境。
範例：輸入 120、180、0 後，清單中應有 120 和 180，總額是 300 元。
'''

'''
題目 31：記錄每日餐費（普通）
建立空的 expenses 清單，以及一個用來保存餐費總和的變數。
使用 while 持續詢問使用者輸入每天的餐費（整數元）。
輸入 0 時結束，且不要把 0 加進清單；其他輸入都加入清單並累加總額。
假設使用者只會輸入 0 或正整數。
結束後，如果沒有輸入任何餐費，印出「尚無餐費紀錄」。
否則印出 expenses 清單和餐費總額；若總額大於或等於 500 元，
再印出「本次餐費已達 500 元」，否則印出「本次餐費未達 500 元」。
'''

expenses = []
expense = 10
while expense > 0:
    expense = int(input("請問今天的餐費幾元?"))
    if expense == 0:
        break
    else:
        expenses.append(expense)
if (len(expenses)) > 0:
    print(expenses , f"總共{sum(expenses)}元")
    if sum(expenses) >= 500:
        print("本次餐費已達500元")
    else:
        print("本次餐費未達500元")
else:
    print("尚無餐費紀錄")
