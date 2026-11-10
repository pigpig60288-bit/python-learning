'''
教學：list.pop() 會移除並回傳最後一個項目。物件清單移除後，也能用 for 走訪剩下的物件。

範例：
class Snack:
    def __init__(self, name):
        self.name = name

snacks = [Snack("餅乾"), Snack("果凍")]
snacks.pop()
for snack in snacks:
    print(snack.name)
'''

'''
題目 76：從播放清單移除歌曲
定義 Song 類別，在 __init__ 中儲存歌曲名稱 name。
建立 songs 清單，移除清單中的最後一首歌曲，再逐一印出剩下歌曲的名稱。
使用清單的 pop() 移除項目；不要直接把預期輸出寫死。

標準輸入範例 1：

songs = [Song("月亮代表我的心"), Song("你是我的眼")]

預期輸出 1：

月亮代表我的心

標準輸入範例 2：

songs = [Song("你是我的眼"), Song("月亮代表我的心")]

預期輸出 2：

你是我的眼
'''
class Song:
    def __init__(self, name):
        self.name = name

songs = [Song("月亮代表我的心"), Song("你是我的眼")]
songs.pop()
for song in songs:
    print(song.name)