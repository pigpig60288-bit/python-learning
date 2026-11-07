# 教學：可以在 for 迴圈裡放 if，只對符合條件的項目執行動作。
# 範例：
# temperatures = [10, 14, 25]
# for temperature in temperatures:
#     if temperature < 15:
#         print(temperature)
# 這段程式只會印出小於 15 的溫度。
#
# 題目 17：找出高分
# 使用 scores 清單，內容為 [72, 85, 91, 64, 80]。
# 使用 for 和 if，逐一檢查分數，只印出大於或等於 80 的分數。
scores = [72, 85, 91, 64, 80]
for score in scores:
    if score >= 80:
        print(score)