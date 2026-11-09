'''
教學：continue 會跳過這一輪迴圈剩下的程式，直接進入下一輪。
範例：
colors = ["紅色", "略過", "綠色"]
for color in colors:
if color == "略過":
continue
print(color)
這會跳過「略過」，印出其他顏色。
'''

'''
題目 27：跳過零分
使用 scores 清單 [10, 0, 8, 0, 6]。
使用 for 和 continue 跳過 0，只印出非零分數。
'''

scores = [10, 0, 8, 0, 6]
for score in scores:
    if score == 0:
        continue
    print(score)
