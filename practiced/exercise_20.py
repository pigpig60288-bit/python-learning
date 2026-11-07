# 教學：for 和 range() 可以讓程式固定重複指定次數。
# 每次迴圈都可以使用 input() 取得一筆資料，再用 append() 加入清單：
# cities = []
# for count in range(2):
#     city = input("輸入一個城市：")
#     cities.append(city)
# print(cities)
# range(2) 會重複兩次；每次輸入都會加到清單末尾。
#
# 題目 20：收集三個電影名稱
# 建立空的 movies 清單，使用 for 迴圈讓使用者輸入三個電影名稱。
# 每輸入一個名稱就用 append() 加進清單，最後印出整個清單。
movies = []
for count in range(3):
    movie = input("輸入一個電影：")
    movies.append(movie)
print(movies)