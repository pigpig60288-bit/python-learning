'''
教學：累加器是用來逐步保存總和的變數，開始時通常設為 0。
每次迴圈把一筆金額加進累加器：
total = 0
for day in range(6, 9):
total = total + 10
print(total)
這個範例模擬連續三天每天存入 10 元，最後印出存款總額。
'''

'''
題目 15：計算連續數字的總和
使用 for 和 range()，計算 1 到 5（包含 1 和 5）的總和。
將結果存入變數並印出；預期輸出為 15。
'''

total = 0
for number in range(1, 6):
    total += number
print(total)
