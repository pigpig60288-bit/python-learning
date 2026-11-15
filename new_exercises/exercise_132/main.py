'''
教學：先處理目前項目，再遞迴處理下一個項目

每次先處理目前位置，再把位置加 1 傳給下一層。
目前位置超過最後一站時，函式就停止：

def show_stops(current, last_stop):
    if current <= last_stop:
        print(f"抵達第 {current} 站")
        show_stops(current + 1, last_stop)

show_stops(2, 4)

'''

'''
題目 132（簡單）：遞迴正向列出數字

輸入一個大於或等於 1 的整數。請定義遞迴函式，依序輸出 1 到輸入數字，
每個數字各占一行。請使用遞迴完成，不可使用 for 或 while。

標準輸入範例 1：

3

預期輸出 1：

1
2
3

標準輸入範例 2：

5

預期輸出 2：

1
2
3
4
5
'''
