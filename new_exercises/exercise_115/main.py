'''
教學：使用索引逐項累加

可以用 while 搭配索引讀取清單，再把每個數字加進總和：

points = [4, 7, 2]
total = 0
index = 0
while index < len(points):
    total += points[index]
    index += 1
print(total)

'''

'''
題目 115：計算三天的閱讀頁數

使用 for 輸入三天各讀了幾頁，存入清單；再使用 while 逐項累加。
最後輸出三天的總頁數，格式為「總頁數：數字」。

標準輸入範例 1：

12
8
15

預期輸出 1：

總頁數：35

標準輸入範例 2：

0
6
9

預期輸出 2：

總頁數：15
'''
