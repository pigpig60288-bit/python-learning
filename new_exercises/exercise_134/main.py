'''
教學：有些遞迴計算要把目前的數值乘上較小問題的結果

例如計算一排座位安排的組合數，每次都乘上目前的座位數。
到沒有座位時，組合數是 1：

def seating_orders(seats):
    if seats == 0:
        return 1
    return seats * seating_orders(seats - 1)

print(seating_orders(3))

'''

'''
題目 134（普通）：遞迴計算階乘

輸入一個大於或等於 0 的整數 N。請定義遞迴函式計算 N 的階乘：
N! = N * (N - 1) * ... * 1，並且 0! = 1。
輸出計算結果，不可使用 for 或 while。

標準輸入範例 1：

0

預期輸出 1：

1

標準輸入範例 2：

5

預期輸出 2：

120
'''
