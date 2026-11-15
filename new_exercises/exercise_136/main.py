'''
教學：用索引遞迴加總清單

索引到達清單長度時，表示沒有剩下的溫度，回傳 0。
其他情況則把目前的溫度加上後面項目的總和：

temperatures = [12, 18, 9]
def total_temperature(index):
    if index == len(temperatures):
        return 0
    return temperatures[index] + total_temperature(index + 1)

print(total_temperature(0))

'''

'''
題目 136（普通）：遞迴加總清單中的數字

先輸入一個正整數代表清單長度，再逐行輸入該數量的整數並存入清單。
請定義遞迴函式，使用索引逐項加總清單並回傳總和。可以使用 for 輸入資料，
但不可使用 for、while 或 sum() 走訪或加總清單。

標準輸入範例 1：

4
3
6
2
5

預期輸出 1：

16

標準輸入範例 2：

3
10
-2
7

預期輸出 2：

15
'''
