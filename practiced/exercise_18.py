# 教學：f-string 可以在文字中直接放入變數。
# 在字串前加 f，並把變數名稱放在大括號 {} 中：
# city = "台南"
# days = 3
# print(f"我在{city}玩了{days}天")
# Python 會把大括號中的變數值放進文字裡。
#
# 題目 18：顯示遊戲分數
# 建立 game_name 和 score 兩個變數，分別存一個遊戲名稱和整數分數。
# 使用 f-string 印出「我在○○得到○分。」；將 ○○ 換成變數的值。
game_name = "世界計畫"
score = 100057300
print(f"我在{game_name}得到{score}分。")