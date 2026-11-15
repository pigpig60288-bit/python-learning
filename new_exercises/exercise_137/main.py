'''
教學：遞迴走訪清單時，可以依目前項目決定是否計數

索引到達清單長度時，表示已經檢查完所有飲料。
如果目前項目符合目標，就把 1 加到後續的計數結果：

drinks = ["茶", "水", "茶"]
def count_drinks(index, target):
    if index == len(drinks):
        return 0
    if drinks[index] == target:
        return 1 + count_drinks(index + 1, target)
    return count_drinks(index + 1, target)

print(count_drinks(0, "茶"))

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
