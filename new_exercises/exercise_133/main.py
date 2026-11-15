'''
教學：遞迴可以把目前的數值加上較小問題的結果

遇到停止條件時回傳 0；其他情況則把目前回合的分數，
加上前一回合累積的結果：

def total_round_points(round_number):
    if round_number == 0:
        return 0
    return round_number + total_round_points(round_number - 1)

result = total_round_points(3)
print(result)

'''

'''
題目 133（簡單）：遞迴計算 1 到 N 的總和

輸入一個大於或等於 1 的整數 N。請定義遞迴函式，回傳 1 + 2 + ... + N
的總和，並輸出結果。請使用遞迴，不可使用 for、while 或 sum()。

標準輸入範例 1：

4

預期輸出 1：

10

標準輸入範例 2：

7

預期輸出 2：

28
'''
