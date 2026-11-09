'''
教學：清單切片可以取得清單中一段連續的項目。
寫法是 list[start:end]；start 索引會包含，end 索引不包含。
索引從 0 開始。
範例：
animals = ["貓", "狗", "兔子", "鳥"]
print(animals[1:3])
會取得索引 1 和 2 的項目，也就是「狗」和「兔子」。
'''

'''
題目 32：選出隊員
已知 players 清單如下：
["小安", "小美", "小智", "小華", "小文"]
使用切片取得索引 1 到索引 3 的隊員（包含索引 1，不包含索引 4），
將結果存入 selected_players，並印出 selected_players。
預期輸出：['小美', '小智', '小華']
'''

players = ["小安", "小美", "小智", "小華", "小文"]
selected_players = players[1:4]
print(selected_players)
