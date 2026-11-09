'''
教學：用 * 做乘法。把單價乘上數量，就能算出總價。
數字要和文字用 + 串接時，先用 str() 把數字轉成文字。
'''

'''
題目 6：一杯珍珠奶茶 55 元，買 3 杯。計算總價並印出購買數量和總價。

標準輸入範例 1：
bubble_milk_tea_price = 55
cups = 3

預期輸出 1：
你買了3杯珍珠奶茶，總共165元。

標準輸入範例 2：
bubble_milk_tea_price = 60
cups = 2

預期輸出 2：
你買了2杯珍珠奶茶，總共120元。
'''

bubble_milk_tea_price = 55
cups = 3
total_price = bubble_milk_tea_price * cups
print("你買了" + str(cups) + "杯珍珠奶茶，總共" + str(total_price) + "元。")
