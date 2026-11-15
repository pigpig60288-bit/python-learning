'''
教學：遞迴函式可以依照目前項目選擇不同結果

處理清單時，可以先檢查目前項目，再把本次結果和後續遞迴結果合併：

values = [4, 9, 2]
def count_large(index):
    if index == len(values):
        return 0
    if values[index] >= 5:
        return 1 + count_large(index + 1)
    return count_large(index + 1)

'''

'''
題目 137（普通偏難）：遞迴計算目標數字出現幾次

先輸入清單長度，再逐行輸入整數建立清單；最後輸入一個目標數字。
請使用遞迴函式和索引，回傳目標數字在清單中出現的次數。可以使用 for
輸入資料，但不可使用 for、while 或 count() 走訪清單或統計次數。

標準輸入範例 1：

5
2
7
2
4
2
2

預期輸出 1：

3

標準輸入範例 2：

4
1
3
5
7
2

預期輸出 2：

0
'''
