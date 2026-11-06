# 教學：while 迴圈會在條件為 True 時重複執行縮排區塊中的程式。
# 基本寫法：
# number = 3
# while number > 0:
#     print(number)
#     number = number - 1
# 每次迴圈都要更新用來判斷的變數，否則條件可能一直成立而無限重複。
#
# 題目 10：倒數計時
# 使用 while 迴圈，從 5 開始依序印出 5、4、3、2、1，最後印出「開始！」。
# 每個數字和「開始！」都要各自印在一行。
#
# 預期輸出：
# 5
# 4
# 3
# 2
# 1
# 開始！
number = 5
while number > 0:
    print(number)
    number -= 1
print("開始！") 