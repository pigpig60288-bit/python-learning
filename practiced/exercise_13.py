# 教學：while 會在條件成立時重複執行；迴圈中要再次取得輸入，才能讓條件有機會改變。
# 可以設定一個「停止字詞」作為結束訊號：
# command = input("輸入 go 繼續，其他內容結束：")
# while command == "go":
#     print("繼續執行")
#     command = input("輸入 go 繼續，其他內容結束：")
#
# list 的 append() 可以把一個值加到清單最後面：
# colors = ["紅色"]
# colors.append("藍色")
# print(colors)
# 上面的例子分開示範輸入控制迴圈與加入清單；請在題目中自行把它們組合起來。
#
# 題目 13：收集喜歡的動物
# 建立一個空的 animals 清單。
# 重複詢問使用者輸入一種喜歡的動物；每次輸入後將動物加入清單。
# 當使用者輸入「停止」時，結束輸入，不要把「停止」加入清單。
# 結束後印出收集到的 animals 清單。
#
# 範例：輸入「貓」、「狗」、「停止」後，清單中應只有「貓」和「狗」。


animals = []
finish = "結束"
pet = input("請輸入一隻自己喜歡的動物，輸入結束即完成清單:")
while pet != finish:
    animals.append(pet)
    pet = input("請輸入一隻自己喜歡的動物，輸入結束即完成清單:")
print(animals)

# animals = []
# pet = ""
# while pet != "結束":
#     animals.append(pet)
#     pet = input("請輸入一隻自己喜歡的動物，輸入結束即完成清單:")
# print(animals[1:])