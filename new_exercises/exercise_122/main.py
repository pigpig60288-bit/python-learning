'''
教學：用兩種迴圈找清單中的最大值與最小值

先把第一個項目當作目前的最大值和最小值，再用 while 逐項比較：

heights = [8, 3, 6]
largest = heights[0]
smallest = heights[0]
index = 1
while index < len(heights):
    if heights[index] > largest:
        largest = heights[index]
    if heights[index] < smallest:
        smallest = heights[index]
    index += 1

'''

'''
題目 122：整理每日最低溫和最高溫

先輸入一個正整數代表天數，再使用 for 輸入每天的氣溫並存入清單。
接著用 while 走訪清單，找出最低溫和最高溫。最後用 print() 的 sep
參數將兩項結果放在同一行，中間以「；」分隔。

標準輸入範例 1：

4
18
25
13
20

預期輸出 1：

最低溫：13；最高溫：25

標準輸入範例 2：

3
7
11
9

預期輸出 2：

最低溫：7；最高溫：11
'''
