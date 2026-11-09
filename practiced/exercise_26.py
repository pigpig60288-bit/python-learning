'''
教學：break 可以立刻結束目前所在的迴圈。
範例：
for number in range(2, 8):
if number == 5:
print("找到 5")
break
當 number 等於 5 時，break 會停止迴圈，不再檢查後面的數字。
'''

'''
題目 26：在清單中找到指定動物
建立 animals 清單，內容為 ["海豚", "狐狸", "企鵝", "長頸鹿"]。
使用 for 逐項檢查清單；找到「企鵝」時印出「找到了」，並用 break 結束迴圈。
'''

animals = ["海豚", "狐狸", "企鵝", "長頸鹿"]
for animal in animals:
    if animal == "企鵝":
        print("找到了")
        break
