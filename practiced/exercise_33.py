# 教學：切片 list[start:end] 會取出從 start 開始、到 end 前一格的項目。
# 清單索引從 0 開始，因此 list[1:3] 會取出索引 1 和 2。
# 範例：
# snacks = ["餅乾", "蛋糕", "布丁", "果凍"]
# print(snacks[0:2])
# 會印出 ["餅乾", "蛋糕"]。
#
# 題目 33：挑選旅遊景點
# 建立 places 清單，依序放入「海邊」、「森林」、「美術館」、「夜市」、「公園」。
# 使用切片取得索引 2 和 3 的景點，存入 selected_places，並印出它。
# 預期輸出：['美術館', '夜市']
places = ["海邊" , "森林" , "美術館" , "夜市" , "公園"]
selected_places = places[2:4]
print(selected_places)