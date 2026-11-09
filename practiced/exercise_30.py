'''
教學：這是一題綜合練習，會用到已教過的 while、input()、int()、
list、append()、sum()、len() 和 f-string。
先用 while 收集資料並 append() 到清單；完成後可用 sum() 算總和、
len() 算筆數，最後用 f-string 把結果印成一句話。
範例：
scores = [8, 12]
print(f"共記錄{len(scores)}筆，合計{sum(scores)}分")
這個範例示範清單統計和 f-string；題目使用不同情境與資料。
'''

'''
題目 30：記錄每天的運動分鐘數
建立空的 minutes 清單，使用 while 持續詢問使用者輸入運動分鐘數。
輸入 0 時停止，且不要把 0 加進清單；其他輸入都轉成整數後加入清單。
輸入結束後，使用 len() 和 sum() 計算記錄了幾天、總共運動幾分鐘，
再用 f-string 印出這兩個結果。
假設使用者只會輸入 0 或正整數。
'''

minutes = []
minute = 20
while minute != 0:
    minute = int(input("請問你運動多久?"))
    if minute > 0:
        minutes.append(minute)
    else:
        break
print(f"共紀錄{len(minutes)}天，合計運動{sum(minutes)}分鐘。")
