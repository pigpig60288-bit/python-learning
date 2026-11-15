'''
教學：外層和內層可以使用不同種類的迴圈

外層 for 可以決定要處理幾行，內層 while 則逐格處理一行：

for row in range(1, 3):
    column = 1
    while column <= 4:
        print("o", end="")
        column += 1
    print()

'''

'''
題目 116：印出長方形座位圖

輸入兩個正整數，依序代表列數和每列座位數。使用 for 和 while
印出長方形座位圖，每個座位用 O 表示，每列結束後換行。

標準輸入範例 1：

2
4

預期輸出 1：

OOOO
OOOO

標準輸入範例 2：

3
2

預期輸出 2：

OO
OO
OO
'''
