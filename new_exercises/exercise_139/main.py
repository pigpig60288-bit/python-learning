'''
教學：有些問題可以拆成兩種較小的情況

例如一次可以爬 1 階或 2 階。到第 n 階的方法數，
等於從前一階走 1 階的方法數，加上從前兩階走 2 階的方法數：

def ways_to_climb(stairs):
    if stairs <= 2:
        return stairs
    return ways_to_climb(stairs - 1) + ways_to_climb(stairs - 2)

print(ways_to_climb(4))

'''

'''
題目 139（困難）：計算費波那契數

定義費波那契數列：F(0) = 0、F(1) = 1；當 N 大於 1 時，
F(N) = F(N - 1) + F(N - 2)。
輸入一個大於或等於 0 的整數 N，請用遞迴回傳並輸出 F(N)。
不可使用 for 或 while。

標準輸入範例 1：

6

預期輸出 1：

8

標準輸入範例 2：

8

預期輸出 2：

21
'''
